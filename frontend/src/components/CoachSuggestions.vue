<script setup>
  const emit = defineEmits(["select"])
</script>

<template>
    <ul id="coach-suggestions">
        <li class="coach-suggestion" @click="$emit('select', 'Why is this a scam')">Why is this a scam?</li>
        <li class="coach-suggestion" @click="$emit('select', 'What’s the safest next step?')">What’s the safest next step?</li>
        <li class="coach-suggestion" @click="$emit('select', 'Should I reply? If yes, how?')">Should I reply? If yes, how?</li>
    </ul>
</template>

<style scoped>
ul {
    list-style-type: none;
    display: flex;
    justify-content: space-evenly;
}
li {
    color: #F9F7F7;
    background-color: #112D4E;
    font-size: 26px;
    padding: 15px;
    border-radius: 15px;
}

li:hover {
    filter: brightness(110%)
}
</style>
