import string

import joblib
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

MODEL, stemmer, stopwords_set, vectorizer = joblib.load("models/model.pkl")


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
    text: str = "empty"


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
