<script setup>
import { ref } from 'vue'
defineProps({progress : Number})
</script>

<template>
    <div id="progress">
        <p>{{ progress }}%</p>
        <div id="progress-bar" :style="{ '--progress': progress + '%'}" :class="progress > 50 ? `red` : `green`"></div>
    </div>
</template>

<style scoped>
#progress-bar {
    background: #fff;
    border-radius: 13px;
    height: 20px;
    width: 100%;
    border: 3px solid black;
}

#progress-bar:after {
    content: "";
    display: block;
    width: progress + '%';
    height: 100%;
    width: var(--progress);
    border-radius: 9px;
}

#progress {
    display: flex;
    gap: 10px;
    align-items: baseline;
}

p {
    font-size: 25px;
    color: #2C2C2C;
}

.green:after {
    background: #49a078;
}

.red:after {
    background: #C94C4C;
}
</style>
