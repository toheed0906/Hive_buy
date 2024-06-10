<template>
  <SearchAndCategory class="d-flex" />
  <div>
    <div class="container d-flex justify-content-between pt-4 no-margin">
      <h4>Products : ({{ store.state.totalProducts }} Products)</h4>
      <div>
        <OrderingAndPagination />
      </div>
    </div>
    <div class="container d-flex justify-content-center">
      <Sidebar />
      <Products />
    </div>
  </div>
</template>

<script setup>
import { defineComponent, onMounted } from "vue";
import { useStore } from "vuex";
import Sidebar from "@/components/Sidebar.vue";
import SearchAndCategory from "@/components/SearchAndCategory.vue";
import Products from "@/components/Products.vue";
import OrderingAndPagination from "@/components/OrderingAndPagination.vue";
const store = useStore();
onMounted(() => {
  store.dispatch("fetchProducts");
});

defineComponent({
  components: {
    Sidebar,
    SearchAndCategory,
    Products,
    OrderingAndPagination,
  },
});
</script>
