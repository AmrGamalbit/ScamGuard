<script setup>
import QuizQuestion from "./QuizQuestion.vue";
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
        <br>
        <QuizQuestion />
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
