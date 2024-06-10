<template>

    <div class="bg-smoke full-width category-modal">
        <div class="d-flex pointer-cursor no-text-wrap pb-2">
            <div v-for="cat in store.state.categories" class="cat-box">
                <h2 @click="selectCategory(cat.category_name)">{{ cat.category_name }}
                </h2>
                <ul>
                    <li v-for="subcat in cat.sub_category" @click="selectSubCategory(subcat)">
                        {{ subcat }}
                    </li>
                </ul>
            </div>
        </div>
    </div>


</template>

<script setup>
import { useStore } from 'vuex'

const store = useStore()

const selectCategory = (category) => {
    store.commit('setCategoryAndSubCategory', {cat: category , subcat: ''})
    store.dispatch('fetchProducts')
}
const selectSubCategory = (subCategory) => {   
    store.commit('setCategoryAndSubCategory', {cat: '', subcat: subCategory})
    store.dispatch('fetchProducts')
}

</script>
<style scoped>
h2 {
    font-size: 14px;
    font-weight: bold;
}

.cat-box {
    padding-left: 20px;
    padding-right: 20px;
}

.full-width {
    width: 1295px;
}

.bg-smoke {
    --bg-opacity: 1;
    background-color: rgba(242, 242, 242, var(--bg-opacity));
}

.pointer-cursor {
    cursor: pointer;
}

ul li {
    font-size: 12px;
}

.no-text-wrap {
    text-wrap: nowrap;
}

ul {
    padding: 0;
    margin: 0;
    list-style: none;
}

.category-modal {
    position: fixed;
    z-index: 1;
}
</style>