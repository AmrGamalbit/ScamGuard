<script setup></script>

<template>
    <section>
        <div class="detector-box">
            <form action="">
                <div class="detector-form">
                    <label for="detector-box">Detector</label>
                    <textarea name="detector" id="detector-box" placeholder="type the text you wish to detect"></textarea>
                    <button class="detector-type">T</button>
                    <button type="submit" class="submit">Detect</button>
                </div>
            </form>
        </div>
    </section>
</template>

<style scoped>
section {
    padding: 50px;
    background-color: #f9f7f7;
}

div.detector-box {
    position: relative;
    width: 80%;
    margin: 0 auto;
}
textarea {
    width: 100%;
    height: 500px;
    border-radius: 10px;
    border: 3px solid #726E5F;
    padding: 10% 10px;
    font-size: 16px;
}
label {
    position: absolute;
    left: 0;
    right: 0;
    margin-inline: auto;
    width: 50%;
    height: 10%;
    background-color: #dbe2ef;
    font-size: 20px;
    text-align: center;
    border-radius: 0 0 10px 10px;
    border: 3px solid #726E5F;
    font-weight: bold;
    display: flex;
    justify-content: center;
    align-items: center;
}

button {
    color: white;
    background-color: #112d4e;
    border: none;
}

button.submit {
    position: absolute;
    bottom: 5%;
    right: 5%;
    padding: 10px;
    font-size: 20px;
    border-radius: 10px;
}

button.submit:hover {
    filter: brightness(110%);
}

button.detector-type {
    position: absolute;
    top: 0%;
    right: 2%;
    padding: 10px;
    font-size: 16px;
    border-radius:0 0 5px 5px;
}
</style>
