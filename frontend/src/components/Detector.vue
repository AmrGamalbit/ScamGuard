<script setup>
import DetectionResult from "./DetectionResult.vue";
import { ref } from "vue";
const textInput = defineModel();
let progress = ref(0);
let detect = ref(false);
let scamMessage = ref("");
const scamStatuses = [
    { min: 90, max: 100, message: "This is very likely a scam" },
    {
        min: 70,
        max: 89,
        message: "This may be a scam. Please proceed with caution",
    },
    { min: 50, max: 69, message: "This could be a scam" },
    { min: 20, max: 49, message: "This is unlikely to be a scam" },
    { min: 0, max: 19, message: "No scam indicators detected" },
];
async function detectScam() {
    if (textInput.value) {
        detect.value = true;
        const response = await fetch("http://127.0.0.1:8000/scan/text", {
            method: "POST",
            body: JSON.stringify({
                text: textInput.value,
            }),
            headers: {
                "Content-type": "application/json",
            },
        });
        const data = await response.json();
        const scamProbability = Math.round(data["prob_scam"] * 100);
        const status = scamStatuses.find(s => s.min <= scamProbability && scamProbability <= s.max)
        progress.value = scamProbability;
        scamMessage.value = status
    }
}
</script>

<template>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
        href="https://fonts.googleapis.com/css2?family=League+Gothic&display=swap"
        rel="stylesheet"
    />
    <section>
        <div class="detector-box">
            <form action="">
                <div class="detector-form">
                    <label for="detector-box">Detector</label>
                    <textarea
                        name="detector"
                        id="detector-box"
                        placeholder="type the text you wish to detect"
                        v-model="textInput"
                    ></textarea>
                    <button class="detector-type">T</button>
                    <button
                        type="submit"
                        class="submit"
                        @click.prevent="detectScam"
                    >
                        Detect
                    </button>
                </div>
            </form>
        </div>
        <div class="result">
            <br />
            <DetectionResult :progress="progress" :message="scamMessage.message" v-if="detect">
            </DetectionResult>
        </div>
    </section>
</template>

<style scoped>
* {
    font-family: "League Gothic", serif;
}
section {
    padding: 50px;
    background-color: #f9f7f7;
}

div.detector-box {
    position: relative;
    width: 80%;
    margin: 0 auto;
}

div.result {
    width: 80%;
    margin: 0 auto;
}

textarea {
    width: 100%;
    height: 500px;
    border-radius: 10px;
    border: 3px solid #726e5f;
    padding: 10% 10px;
    font-size: 25px;
    color: #2c2c2c;
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
    border: 3px solid #726e5f;
    font-weight: bold;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 28px;
    letter-spacing: 1px;
    color: #1f2933;
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
    font-size: 28px;
    border-radius: 10px;
    letter-spacing: 1px;
}

button.submit:hover {
    filter: brightness(110%);
}

button.detector-type {
    position: absolute;
    top: 0%;
    right: 2%;
    padding: 10px;
    font-size: 20px;
    border-radius: 0 0 5px 5px;
}
</style>
