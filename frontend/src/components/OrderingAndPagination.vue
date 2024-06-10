<template>
  <div class="d-flex">
    <OrderDropDown />
    <Pagination />
  </div>
</template>

<script setup>
import OrderDropDown from "@/components/OrderDropDown.vue";
import Pagination from "@/components/Pagination.vue";
import { defineComponent } from "vue";

defineComponent({
  components: {
    OrderDropDown,
    Pagination,
  },
});
</script>
