<script setup>
import HomeIcon from "./icons/HomeIcon.vue";
import CoachIcon from "./icons/CoachIcon.vue";
import DetectorIcon from "./icons/DetectorIcon.vue";
import GameIcon from "./icons/GameIcon.vue";
</script>
<template>
    <div>
        <ul>
            <div class="right">
                <li>
                    <a href="/"><HomeIcon /></a>
                </li>
            </div>
            <div class="left">
                <li>
                    <a href=""><DetectorIcon /></a>
                </li>
                <li>
                    <a href=""><CoachIcon /></a>
                </li>
                <li>
                    <a href="/game"><GameIcon /></a>
                </li>
            </div>
        </ul>
    </div>
</template>
<style scoped>
ul {
    list-style-type: none;
    background-color: #1f2421;
    display: flex;
    margin: 0;
    padding: 0;
    justify-content: space-between;
    align-items: baseline;
}
ul div.left {
    display: flex;
}
ul li a {
    text-decoration: none;
    display: block;
    padding: 15px;
    color: #f9f7f7;
}
</style>
