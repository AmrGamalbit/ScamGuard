<script setup></script>
<template>
    <div>
        <ul>
            <div class="right">
                <li><a href="">home</a></li>
            </div>
            <div class="left">
                <li><a href="">detector</a></li>
                <li><a href="">coach</a></li>
                <li><a href="">game</a></li>
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
}
ul div.left {
    display: flex;
}
ul li a {
    text-decoration: none;
    display: block;
    padding: 15px;
    color: white;
}
</style>
