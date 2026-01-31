import json
import os
import string
from typing import List

import joblib
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from groq import APIConnectionError, APIStatusError, Groq, RateLimitError
from pydantic import BaseModel

MODEL, stemmer, stopwords_set, vectorizer = joblib.load("models/model.pkl")
load_dotenv()
client = Groq(
    api_key=os.getenv("API_KEY"),
)
AI_MODEL = "moonshotai/kimi-k2-instruct-0905"

SYSTEM_INSTURCTIONS = """
You are a security-aware AI coach specialized in analyzing scams, fraud attempts, and risky interactions.

Your role is to:
- Analyze the user’s input
- Answer the user’s question using simple, clear language
- Help the user achieve their goal
- Provide explanations suitable for students

Output Rules:
- Respond only in valid JSON
- Be concise, clear, and elegant
- No answer may exceed 30 words
- Do not include disclaimers, warnings, or extra commentary
- Do not ask follow-up questions
- Base analysis on real-world scam patterns and security best practices
"""


def preprocess_text(text):
    text_corpus = []
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation)).split()
    text = [stemmer.stem(word) for word in text if word not in stopwords_set]
    text = " ".join(text)
    text_corpus.append(text)
    x_text = vectorizer.transform(text_corpus)
    return x_text


class ScanRequest(BaseModel):
    text: str


class CoachRequest(BaseModel):
    question: str
    text: str


class CoachResponse(BaseModel):
    answer: str


class QuizQuestion(BaseModel):
    question: str
    answers: List[str]
    correct_answer: str
    correct_answer_index: int
    explanation: str


class QuizQuestions(BaseModel):
    questions: List[QuizQuestion]


class TodayTip(BaseModel):
    tip: str


app = FastAPI()
origins = ["http://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def index():
    return "server is running"


@app.post("/scan/text")
async def scan_text(raw_data: ScanRequest):
    data = raw_data.model_dump()
    text = data.get("text")
    X_text = preprocess_text(text)
    prediction = MODEL.predict(X_text)
    label = "scam" if prediction == 1 else "human"
    proba = MODEL.predict_proba(X_text)
    return {
        "text": text.strip(),
        "prediction": int(prediction[0]),
        "label": label,
        "prob_scam": proba[0][1],
        "prob_not_scam": proba[0][0],
    }


@app.post("/ask-coach")
async def ask_coach(raw_data: CoachRequest):
    data = raw_data.model_dump()
    question = data.get("question")
    text = data.get("text")
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": SYSTEM_INSTURCTIONS},
                {
                    "role": "user",
                    "content": f"""
                    Question:
                    {question}

                    Context:
                    {text}
                    """,
                },
            ],
            model=AI_MODEL,
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "Learning_Code",
                    "schema": CoachResponse.model_json_schema(),
                },
            },
        )
        content = chat_completion.choices[0].message.content
        parsed = CoachResponse.model_validate_json(content)
        return parsed

    except APIConnectionError as e:
        raise HTTPException(
            503,
            detail={
                "error": "groq_api_error",
                "message": "Failed to communicate with the AI service. Please check your internet connection and try again.",
                "details": str(e) if str(e) else "Connection timeout or network error",
                "suggestion": "Please wait a moment and try again. If the problem persists, check your API key configuration.",
            },
        )

    except json.JSONDecodeError as e:
        raise HTTPException(
            502,
            detail={
                "error": "model_output_invalid",
                "message": "The AI service returned an invalid response format. This may be a temporary issue.",
                "details": f"JSON parsing failed: {str(e)}",
                "suggestion": "Please try again. If the problem continues, the request may be too complex - try simplifying question.",
            },
        )

    except RateLimitError:
        raise HTTPException(
            429,
            detail={
                "error": "rate_limit_exceeded",
                "message": "Too many requests. Please wait a moment before trying again.",
                "details": "The AI service is temporarily limiting requests to manage load.",
                "suggestion": "Please wait 30-60 seconds before making another request.",
            },
        )

    except APIStatusError as e:
        error_messages = {
            400: "Invalid request to AI service. Please check your input and try again.",
            401: "Authentication failed. Please check your API key configuration.",
            403: "Access forbidden. Please check your API key permissions.",
            404: "AI service endpoint not found. This may indicate a configuration issue.",
            500: "The AI service encountered an internal error. Please try again later.",
            502: "Bad gateway. The AI service is temporarily unavailable.",
            503: "Service unavailable. The AI service is temporarily down.",
            504: "Gateway timeout. The request took too long to process.",
        }
        message = error_messages.get(
            e.status_code, f"The AI service returned an error (status {e.status_code})"
        )

        raise HTTPException(
            502,
            detail={
                "error": "api_status_error",
                "message": message,
                "details": f"HTTP {e.status_code}",
                "suggestion": "Please try again in a few moments. If the problem persists, check your API configuration.",
            },
        )

    except Exception as e:
        raise HTTPException(
            500,
            {
                "error": "unexpected_error",
                "message": "An unexpected error occurred while generating the architecture.",
                "details": str(e),
                "suggestion": "Please try again. If the problem continues, contact support.",
            },
        )


@app.get("/get-questions")
async def get_question():
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": SYSTEM_INSTURCTIONS},
                {
                    "role": "user",
                    "content": """
                Create 10 educational multiple-choice questions to teach students how to recognize scams and stay safe online.

                Requirements:
                - Use real-life scenarios (texts, emails, social media messages, phone calls).
                - Test decision-making: when to respond, when to ignore, and when to report.
                - Each question must have 4 answer choices (A–D).
                - Only one correct answer per question.
                - After each question, include:
                  - The correct answer
                  - A short explanation (1–2 sentences) explaining why it is correct
                - Keep the content age-appropriate and easy to understand.
                """,
                },
            ],
            model=AI_MODEL,
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "Learning_Code",
                    "schema": QuizQuestions.model_json_schema(),
                },
            },
        )
        content = chat_completion.choices[0].message.content
        parsed = QuizQuestions.model_validate_json(content)
        return parsed

    except APIConnectionError as e:
        raise HTTPException(
            503,
            detail={
                "error": "groq_api_error",
                "message": "Failed to communicate with the AI service. Please check your internet connection and try again.",
                "details": str(e) if str(e) else "Connection timeout or network error",
                "suggestion": "Please wait a moment and try again. If the problem persists, check your API key configuration.",
            },
        )

    except json.JSONDecodeError as e:
        raise HTTPException(
            502,
            detail={
                "error": "model_output_invalid",
                "message": "The AI service returned an invalid response format. This may be a temporary issue.",
                "details": f"JSON parsing failed: {str(e)}",
                "suggestion": "Please try again.",
            },
        )

    except RateLimitError:
        raise HTTPException(
            429,
            detail={
                "error": "rate_limit_exceeded",
                "message": "Too many requests. Please wait a moment before trying again.",
                "details": "The AI service is temporarily limiting requests to manage load.",
                "suggestion": "Please wait 30-60 seconds before making another request.",
            },
        )

    except APIStatusError as e:
        error_messages = {
            400: "Invalid request to AI service. Please check your input and try again.",
            401: "Authentication failed. Please check your API key configuration.",
            403: "Access forbidden. Please check your API key permissions.",
            404: "AI service endpoint not found. This may indicate a configuration issue.",
            500: "The AI service encountered an internal error. Please try again later.",
            502: "Bad gateway. The AI service is temporarily unavailable.",
            503: "Service unavailable. The AI service is temporarily down.",
            504: "Gateway timeout. The request took too long to process.",
        }
        message = error_messages.get(
            e.status_code, f"The AI service returned an error (status {e.status_code})"
        )

        raise HTTPException(
            502,
            detail={
                "error": "api_status_error",
                "message": message,
                "details": f"HTTP {e.status_code}",
                "suggestion": "Please try again in a few moments. If the problem persists, check your API configuration.",
            },
        )

    except Exception as e:
        raise HTTPException(
            500,
            {
                "error": "unexpected_error",
                "message": "An unexpected error occurred while generating the architecture.",
                "details": str(e),
                "suggestion": "Please try again. If the problem continues, contact support.",
            },
        )


@app.get("/get-tip")
async def get_tip():
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": SYSTEM_INSTURCTIONS},
                {
                    "role": "user",
                    "content": """
                    Give a short tip helping students identify scams and stay safe online. Do not exceed 15 words
                """,
                },
            ],
            model=AI_MODEL,
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "Learning_Code",
                    "schema": TodayTip.model_json_schema(),
                },
            },
        )
        content = chat_completion.choices[0].message.content
        parsed = TodayTip.model_validate_json(content)
        return parsed

    except APIConnectionError as e:
        raise HTTPException(
            503,
            detail={
                "error": "groq_api_error",
                "message": "Failed to communicate with the AI service. Please check your internet connection and try again.",
                "details": str(e) if str(e) else "Connection timeout or network error",
                "suggestion": "Please wait a moment and try again. If the problem persists, check your API key configuration.",
            },
        )

    except json.JSONDecodeError as e:
        raise HTTPException(
            502,
            detail={
                "error": "model_output_invalid",
                "message": "The AI service returned an invalid response format. This may be a temporary issue.",
                "details": f"JSON parsing failed: {str(e)}",
                "suggestion": "Please try again.",
            },
        )

    except RateLimitError:
        raise HTTPException(
            429,
            detail={
                "error": "rate_limit_exceeded",
                "message": "Too many requests. Please wait a moment before trying again.",
                "details": "The AI service is temporarily limiting requests to manage load.",
                "suggestion": "Please wait 30-60 seconds before making another request.",
            },
        )

    except APIStatusError as e:
        error_messages = {
            400: "Invalid request to AI service. Please check your input and try again.",
            401: "Authentication failed. Please check your API key configuration.",
            403: "Access forbidden. Please check your API key permissions.",
            404: "AI service endpoint not found. This may indicate a configuration issue.",
            500: "The AI service encountered an internal error. Please try again later.",
            502: "Bad gateway. The AI service is temporarily unavailable.",
            503: "Service unavailable. The AI service is temporarily down.",
            504: "Gateway timeout. The request took too long to process.",
        }
        message = error_messages.get(
            e.status_code, f"The AI service returned an error (status {e.status_code})"
        )

        raise HTTPException(
            502,
            detail={
                "error": "api_status_error",
                "message": message,
                "details": f"HTTP {e.status_code}",
                "suggestion": "Please try again in a few moments. If the problem persists, check your API configuration.",
            },
        )

    except Exception as e:
        raise HTTPException(
            500,
            {
                "error": "unexpected_error",
                "message": "An unexpected error occurred while generating the architecture.",
                "details": str(e),
                "suggestion": "Please try again. If the problem continues, contact support.",
            },
        )
