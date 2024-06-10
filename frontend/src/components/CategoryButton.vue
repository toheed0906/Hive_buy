<template>
  <div>
    <button class="bg-smoke d-flex no-border" id="categoryButton">
      <img src="../assets/menu.png" />
      <h3>{{ name }}</h3>
    </button>
  </div>
</template>

<script setup>
const props = defineProps({
  name: String,
});
</script>

<style scoped>
.no-border {
  border: none;
}

.bg-smoke {
  --bg-opacity: 1;
  background-color: rgba(242, 242, 242, var(--bg-opacity));
}

h3 {
  color: #231f20;
  font-size: 17px;
  margin-left: 8px;
  margin-top: 16px;
}

img {
  height: 24px;
  width: 24px;
  margin-top: 12px;
  margin-left: 10px;
}
</style>
