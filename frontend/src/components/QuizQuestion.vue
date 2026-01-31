<script setup>
import { ref } from "vue";
const props = defineProps({
    question: String,
    answers: Array,
    correctAnswerIndex: Number,
});
const emit = defineEmits(["next"])
const answerColor = ref("");
const selectedIndex = ref("")
const isAnsweredCorrectly = ref(false)
function checkAnswer(index) {
    if (index == props.correctAnswerIndex) {
        answerColor.value = "green";
        isAnsweredCorrectly.value = true
    } else {
        answerColor.value = "red";
        isAnsweredCorrectly.value = false
    }
    selectedIndex.value = index
    emit('next', isAnsweredCorrectly.value)
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
        <div id="question-container">
            <div id="question-border"></div>
            <p id="question">
                {{ question }}
            </p>
        </div>
        <ul id="question-answers">
            <li
                :class="(selectedIndex == index) ? `question-answer ${answerColor}` : `question-answer`"
                v-for="(answer, index) in answers"
                @click="checkAnswer(index)"
            >
                {{ answer }}
            </li>
        </ul>
    </section>
</template>

<style scoped>
#question-border {
    width: 100%;
    height: 20px;
    background-color: #d9d9d9;
    margin-bottom: 30px;
}
p {
    font-size: 20px;
    font-family: "Inter" serif;
    text-align: center;
}
ul {
    list-style-type: none;
    display: grid;
    grid-template-columns: 1fr 1fr;
    padding: 30px;
    gap: 50px;
    font-family: "Inter" serif;
    font-size: 16px;
}
li {
    border: solid black 3px;
    border-radius: 10px;
    padding: 10px;
}
li:hover {
    cursor: pointer;
    filter: brightness(110%)
}
.green {
    background: #49a078;
}

.red {
    background: #c94c4c;
}
</style>
