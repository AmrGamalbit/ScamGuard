<script setup>
import { ref } from 'vue'
  const progress = ref(89)
</script>

<template>
    <div id="progress">
        <p>{{ progress }}%</p>
        <div id="progress-bar" :style="{ '--progress': progress + '%'}"></div>
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
    background: #49a078;
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
    color: #1F2421;
}
</style>
