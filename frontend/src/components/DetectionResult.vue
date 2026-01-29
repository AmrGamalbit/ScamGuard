<script setup>
import { ref } from "vue";
defineProps({ progress: Number, message: String });
</script>

<template>
    <div id="progress">
        <p>{{ progress }}%</p>
        <div
            id="progress-bar"
            :style="{ '--progress': progress + '%' }"
            :class="progress > 50 ? `red` : `green`"
        ></div>
    </div>
    <p id="tag" :class="progress > 50 ? `red` : `green`">
        {{ message }}
    </p>
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
    width: progress + "%";
    height: 100%;
    width: var(--progress);
    border-radius: 5px;
}

#progress {
    display: flex;
    gap: 10px;
    align-items: baseline;
}

p {
    font-size: 25px;
    color: #2c2c2c;
}

.green:after {
    background: #49a078;
}

.red:after {
    background: #c94c4c;
}

.red {
    color: #c94c4c;
}

.green {
    color: #49a078;
}

#tag {
    text-align: center;
    padding-top: 10px;
}
</style>
