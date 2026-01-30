<script setup>
import CoachSuggestions from "./CoachSuggestions.vue";
</script>

<template>
    <CoachSuggestions></CoachSuggestions>
    <form action="" id="ask-coach-smallbox">
        <div id="coach-explaination">
            <p>
                Lorem, ipsum dolor sit amet consectetur adipisicing elit. Cumque
                ad necessitatibus accusamus nihil dolorum, fugit ex alias
                inventore facilis nobis tempora, minima quam, eius nulla
                veritatis nesciunt in? Aliquid, perferendis?
            </p>
        </div>
        <label for="coach">Hello</label>
        <textarea
            name="coach"
            id="ask-coach-textbox"
            placeholder="ask coach anything"
        ></textarea>
        <button type="submit">Submit</button>
    </form>
</template>

<style scoped>
* {
    font-family: "League Gothic", serif;
}
section {
    padding: 50px;
    background-color: #f9f7f7;
}
label {
    display: none;
}
form {
    display: flex;
    flex-direction: column;
    margin-top: 30px;
    position: relative;
}

div {
    height: 100px;
    padding: 10px;
    font-size: 25px;
    border-radius: 10px 10px 0 0;
    border: solid black 3px;
}
textarea {
    position: relative;
    padding: 10px;
    font-size: 25px;
    width: 100%;
    border: solid 3px black;
    border-radius: 0 0 10px 10px;
    border-top: none;
}
button {
    position: absolute;
    bottom: 5%;
    right: 5%;
    padding: 10px;
    border-radius: 10px;
    border: none;
    background-color: #112D4E;
    color: white;
}
</style>
