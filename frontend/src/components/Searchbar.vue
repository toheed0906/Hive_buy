<template>
       <div>
        <h3> {{ title }}</h3>
        <div class="rounded-full bg-smoke-100 d-flex justify-content-center py-2 border border-dark-b ">
            <input type="text" :placeholder=placeholder class="app-input bg-smoke-100  text-center" :value=value @change="$emit('input', $event.target.value)" >
            <i  class="fa fa-search search-icon"></i>
        </div>
    </div>
</template>

<script setup>
const props = defineProps(
    {
        title: String,
        placeholder: String,
        value: {
            type: [Number, String],
            default: null
        }
    }
)
</script>

<style scoped>
h3 {
    font-size: 1.125rem;
    color: #231f20;
    padding-bottom: 12px;
}
.fullWidth
{
    width: 100%;
}
.rounded-full {
    border-radius: 9999px;
    width: 100%;
}

.app-input {
    border-radius: 9999px;
    padding-left: .75rem;
    padding-right: .75rem;
    padding-top: 2px;
    width: 100%;
    border: none;
    outline: none;
}
.bg-smoke-100 {
    --bg-opacity: 1;
    background-color: rgba(242, 242, 242, var(--bg-opacity));
}
.border-dark-b {
    border-color: rgba(35, 31, 32, .15);
}

.search-icon{
    padding-top: 5px;
    padding-right: 12px;
    opacity: .5;
}
</style>