<template>
    <div class="d-flex justify-cotent-center py-1 checkbox-wrapper">
        <input type="checkbox" class="w-5 h-5" :value="name" :checked="checked" @change="updateValue">
        <span class="pl-4">
            <img v-if="name == 'In USA'"  src="../assets/usa.svg" height="24px" width="24px" alt="" class="mb-1"> {{ name }}</span>
   </div>
</template>

<script setup>

import { defineEmits } from 'vue';
defineProps({
  name: String,
  checked: Boolean,
});
const emit = defineEmits(['update:checked']);
const updateValue = (event) => {
  emit('update:checked', event.target.checked);
}

</script>

<style scoped>
.checkbox-wrapper {
    position: relative;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    cursor: pointer;
}
.checkbox-wrapper input{
    height: 18px;
    width: 18px;
    cursor: pointer;
    margin-top: 2px;
    margin-right:2px;
    margin-left: 4px;
}
span
{
    padding-left: 16px;
    font-size: 16px;
}
</style>