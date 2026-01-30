<script setup>
import CoachSuggestions from "./CoachSuggestions.vue";
import SendIcon from "./icons/SendIcon.vue";
</script>

<template>
    <CoachSuggestions></CoachSuggestions>
    <form action="" id="ask-coach-smallbox">
        <div id="coach-explaination">
            <img src="./icons/CoachQuickHelpIcon.png" alt="coach image">
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
        <button type="submit"><SendIcon></SendIcon></button>
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
    color: #2c2c2c;
    display: flex;
    align-items: center;
}

div img {
    width: 100px;
    height: 100px;
}

textarea {
    position: relative;
    padding: 10px;
    font-size: 25px;
    width: 100%;
    border: solid 3px black;
    border-radius: 0 0 10px 10px;
    border-top: none;
    color: #000;
}
button {
    position: absolute;
    bottom: 5%;
    right: 5%;
    border-radius: 10px;
    border: solid 3px black;
    color: #112d4e;
}
button:hover {
    filter: brightness(110%);
}
</style>
