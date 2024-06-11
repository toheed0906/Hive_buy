<template>
  <div>
    <div class="d-flex justify-content-between">
      <button
        class="py-2 px-3 mx-3 no-border full-rounded-border"
        @click="goToPerviousPage"
      >
        <img src="https://thebuyhive.com/buy/img/chevronLeft.c50c4a36.svg" />
      </button>
      <div class="py-2 px-3 bg-smoke full-rounded-border">
        {{ page }}
      </div>
      <div class="total-page">of {{ totalPages }}</div>

      <button class="py-2 px-3 no-border full-rounded-border ml-4" @click="goToNextPage">
        <img src="https://thebuyhive.com/buy/img/chevronRight.b3ce29d8.svg" />
      </button>
    </div>
  </div>
</template>

<script setup>
import { computed } from "vue";
import { useStore } from "vuex";
const store = useStore();
const page = computed(() => store.state.filters["page"]);
const totalPages = computed(() => Math.ceil(store.state.totalProducts / 9));

const goToPerviousPage = () => {
  if (page.value > 1) {
    store.state.filters["page"] = page.value - 1;
    store.dispatch("fetchProducts");
  }
};
const goToNextPage = () => {
  if (page.value < totalPages.value) {
    store.state.filters["page"] = page.value + 1;
    store.dispatch("fetchProducts");
  }
};
</script>
<style scoped>
.no-border {
  border: none;
}

.full-rounded-border {
  border-radius: 9999px;
}

.bg-smoke {
  --bg-opacity: 1;
  background-color: rgba(242, 242, 242, var(--bg-opacity));
  padding: 10px 20px;
}

.total-page {
  display: flex;
  align-items: center;
  font-size: 18px;
  padding-left: 8px;
  padding-right: 12px;
}
</style>
