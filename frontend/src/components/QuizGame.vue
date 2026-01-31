<script setup>
import QuizQuestion from "./QuizQuestion.vue";
import { ref } from "vue";
const questions = ref([]);

async function fetchQuestions() {
    const response = await fetch("http://127.0.0.1:8000/get-questions");
    const data = await response.json();
    questions.value = data["questions"];
}

const currentQuestionIndex = ref(0);
const question = ref("");
const answers = ref([]);
const correctAnswerIndex = ref(0);
const score = ref(0);
const explanation = ref("");

async function startQuiz() {
    await fetchQuestions();
    getNextQuestion();
}

function getNextQuestion(isAnsweredCorrectly) {
    if (isAnsweredCorrectly) {
        score.value += 1;
    }
    if (currentQuestionIndex.value < questions.value.length) {
        console.log(questions.value[currentQuestionIndex.value].question);
        question.value = questions.value[currentQuestionIndex.value].question;
        answers.value = questions.value[currentQuestionIndex.value].answers;
        correctAnswerIndex.value =
            questions.value[currentQuestionIndex.value].correct_answer_index;
        explanation.value =
            questions.value[currentQuestionIndex.value].explanation;
        currentQuestionIndex.value += 1;
    } else {
        console.log("We reach the end");
    }
}
startQuiz();
</script>

<template>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
        href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap"
        rel="stylesheet"
    />
    <section>
        <h2>Interactive Game</h2>
        <p>Play and compete</p>
        <br />
        <p>{{ score }}</p>
        <QuizQuestion
            :question
            :answers
            :correctAnswerIndex
            :explanation
            @next="getNextQuestion"
        />
    </section>
</template>

<style scoped>
section {
    background-color: #f9f7f7;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
    padding: 50px;
}
h2 {
    font-family: "Inter";
    color: #2c2c2c;
    font-weight: 600;
    font-size: 40px;
    letter-spacing: 2px;
}
p {
    font-family: "Inter";
    color: #2c2c2c;
    font-weight: 200;
    font-size: 30px;
}
</style>
