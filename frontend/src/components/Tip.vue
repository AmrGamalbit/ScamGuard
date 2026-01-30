<script setup></script>

<template>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
        href="https://fonts.googleapis.com/css2?family=League+Gothic&display=swap"
        rel="stylesheet"
    />
    <link
        href="https://fonts.googleapis.com/css?family=Leckerli One"
        rel="stylesheet"
    />
    <section>
        <div class="tip-frame">
            <div class="tip-container">
                <h2>Today's Tip</h2>
            </div>
            <p>Never give your password to anyone!</p>
        </div>
    </section>
</template>

<style scoped>
section {
    border-radius: 10px;
    padding: 50px;
    background-color: #f9f7f7;
    height: 200px;
}
div.tip-frame {
    position: relative;
    background-color: #112d4e;
    margin: 0 auto;
    width: 80%;
    height: 100%;
    border-radius: 10px;
    padding: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #1f2933;
}
div.tip-container {
    position: absolute;
    top: 0;
    left: 0;
    background-color: #dbe2ef;
    padding: 10px 20px;
    border-radius: 10px 0 30px 0;
    font-family: "Leckerli One";
}
p {
    color: white;
    text-align: center;
    font-size: 35px;
    font-weight: 500;
    font-family: "League Gothic", serif;
}
</style>
