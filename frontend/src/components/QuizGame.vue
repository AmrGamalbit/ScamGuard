<script setup>
import QuizQuestion from "./QuizQuestion.vue";
import { ref } from "vue";
const questions = [
    {
        question: "what is scam?",
        answers: ["don't know", "don't care", "don't know", "don't know"],
        correctAnswer: 1,
    },
    {
        question: "what is safe?",
        answers: ["don't know", "don't care", "don't know", "don't know"],
        correctAnswer: 0,
    },
    {
        question: "fd is safe?",
        answers: ["don't know", "don't care", "don't know", "don't know"],
        correctAnswer: 0,
    },
];

const currentQuestionIndex = ref(0);
const question = ref("");
const answers = ref([]);
const correctAnswerIndex = ref(0);
const score = ref(0);

function startQuiz() {
    getNextQuestion();
}

function getNextQuestion(isAnsweredCorrectly) {
    if (isAnsweredCorrectly) {
        score.value += 1;
    }
    if (currentQuestionIndex.value < questions.length) {
        question.value = questions[currentQuestionIndex.value].question;
        answers.value = questions[currentQuestionIndex.value].answers;
        correctAnswerIndex.value =
            questions[currentQuestionIndex.value].correctAnswer;
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
