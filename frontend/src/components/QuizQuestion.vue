<script setup></script>

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
                A Person ask you to give him a password, what should you do?
            </p>
        </div>
        <ul id="question-answers">
            <li class="question-answer">Give him the password</li>
            <li class="question-answer">Give him the password</li>
            <li class="question-answer">Give him the password</li>
            <li class="question-answer">Give him the password</li>
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
    font-family: inter;
}
ul {
    list-style-type: none;
    display: grid;
    grid-template-columns: 1fr 1fr;
    padding: 30px;
    gap: 50px;
    font-family: inter;
    font-size: 16px;
}
li {
    border: solid black 3px;
    border-radius: 10px;
    padding: 10px;
}
li:hover {
    background-color: #d9d999;
    cursor: pointer;
}
</style>
