<template>
    <select v-model="store.state.selectedCategoryName"
        class="no-border no-outline white-bg less-opacity">
        <option value="" > All Categories</option>
        <option class="text-black p-2"  v-for="cat in store.state.categories "
            :value="cat.category_name"> {{
                cat.category_name }}
        </option>
    </select>
</template>

<script setup>
import { onMounted } from 'vue'
import { useStore } from 'vuex'
import axios from 'axios'

const store = useStore()
onMounted(async () => {
  try {
    const response = await axios.get(store.state.categoryUrl);
    store.commit('setCategories', response.data)
  } catch (error) {
    console.log(error);
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
.less-opacity
{
    opacity: .5; 
}
.white-bg{
    background-color: white;
    width: 250px;
}
</style>