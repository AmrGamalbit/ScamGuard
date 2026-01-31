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
const quizStatus = ref("notStarted");

async function startQuiz() {
    quizStatus.value = "inProgress";
    currentQuestionIndex.value = 0;
    await fetchQuestions();
    getNextQuestion();
}

function getNextQuestion(isAnsweredCorrectly) {
    if (isAnsweredCorrectly) {
        score.value += 1;
    }
    if (currentQuestionIndex.value < questions.value.length) {
        question.value = questions.value[currentQuestionIndex.value].question;
        answers.value = questions.value[currentQuestionIndex.value].answers;
        correctAnswerIndex.value =
            questions.value[currentQuestionIndex.value].correct_answer_index;
        explanation.value =
            questions.value[currentQuestionIndex.value].explanation;
        currentQuestionIndex.value += 1;
    } else {
        displayResult();
    }
}

function displayResult() {
    quizStatus.value = "finished";
}
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
        <div v-if="quizStatus == 'notStarted'" id="quiz-instructions">
            <h2>Game Instructions</h2>
            <ul>
                <li>
                    Read each question carefully and select the correct answer
                    from the available options.
                </li>
                <li>Your score increases for every correct answer.</li>
                <li>
                    Try to answer all questions and see your final score at the
                    end of the quiz.
                </li>
            </ul>
            <button @click="startQuiz" class="quiz-button">Start Quiz</button>
        </div>
        <div v-else-if="quizStatus == 'inProgress'" id="quiz-progress">
            <p>Your current score: {{ score }}</p>
            <QuizQuestion
                :question
                :answers
                :correctAnswerIndex
                :explanation
                @next="getNextQuestion"
            />
        </div>
        <div v-else id="quiz-end">
            <div id="final-score-container">
                <h2>Finished the quiz</h2>
                <p>Your final score: {{ score }}</p>
            </div>
            <button @click="startQuiz" class="quiz-button">Retry</button>
        </div>
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

#quiz-end {
    display: flex;
    flex-direction: column;
    gap: 20px;
    align-items: center;
}

#quiz-end h2,
#quiz-instructions h2 {
    font-size: 30px;
    font-weight: 400;
    margin-bottom: 20px;
}

.quiz-button {
    color: #f9f7f7;
    background-color: #112d4e;
    font-size: 15px;
    padding: 15px;
    border-radius: 15px;
    border: none;
}

.quiz-button:hover {
    filter: brightness(110%);
}

#final-score-container {
    background-color: #dbe2ef;
    padding: 40px;
    border-radius: 20px;
    text-align: center;
}

ul {
    list-style-type: none;
    display: flex;
    flex-direction: column;
    margin-bottom: 30px;
}

p {
    font-family: "Inter";
    color: #2c2c2c;
    font-weight: 200;
    font-size: 30px;
}
</style>
