<script setup>
import Navbar from "@/components/Navbar.vue";
import { RouterView } from "vue-router";
</script>

<template>
    <Navbar />
    <RouterView />
</template>

<style>
* {
    margin: 0px;
    padding: 0px;
    box-sizing: border-box;
}
body {
    background-color: #f9f7f7;
}
</style>
