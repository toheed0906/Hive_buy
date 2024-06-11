<template>
  <select
    v-model="store.state.selectedCategoryName"
    class="no-border no-outline white-bg less-opacity"
  >
    <option value="">All Categories</option>
    <option class="text-black p-2" v-for="cat in categories" :value="cat.category_name">
      {{ cat.category_name }}
    </option>
  </select>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useStore } from "vuex";
import axios from "axios";
import { HTTP } from "@/request.js";

const store = useStore();
const categories = ref([]);

onMounted(async () => {
  try {
    const response = await HTTP.get("/categories/");
    store.commit("setCategories", response.data);
    categories.value = response.data;
  } catch (error) {
    router.push({ name: "ErrorMessage" });
  }
});
</script>

<style scoped>
.no-border {
  border: none;
}

.no-outline {
  outline: none;
}
.less-opacity {
  opacity: 0.5;
}
.white-bg {
  background-color: white;
  width: 250px;
}
</style>
