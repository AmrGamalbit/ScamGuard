<script setup></script>

<template>
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
    background-color: #F9F7F7;
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
}
div.tip-container {
    position: absolute;
    top: 0;
    left: 0;
    background-color: #dbe2ef;
    padding: 10px;
    border-radius: 10px 0 30px 0;
}
p {
    color: white;
    text-align: center;
    font-size: 20px;
    font-weight: 500;
}
</style>
