<template>
  <div class="container">
    <div class="bg-smoke main-search-container round-border">
      <div class="d-flex justify-content-around">
        <div>
          <CategoryButton name="Categories" @click="showCategory" />
        </div>

        <div class="full-rounded-border white-bg py-2 px-2">
          <div class="d-flex">
            <input
              class="no-border no-outline"
              placeholder="What are you looking for?"
              v-model="nameOfProduct"
              @input="handleNameOfProduct"
            />
            <span> | </span>
            <CategoryDropDown />
          </div>
        </div>
        <div>
          <button
            @click="handleNameAndCategory"
            class="no-border no-outline full-rounded-border bg-blue text-white py-2 px-3"
          >
            Search
          </button>
        </div>
      </div>
    </div>
    <CategoryModal class="hidden p-ab" id="categoriesModel" />
  </div>
</template>

<script setup>
import { ref, defineComponent } from "vue";
import { useStore } from "vuex";
import CategoryButton from "@/components/CategoryButton.vue";
import CategoryDropDown from "@/components/CategoryDropDown.vue";
import CategoryModal from "@/components/CategoryModal.vue";

const store = useStore();
const nameOfProduct = ref("");
const filters = ref(store.getters.getFilters);

const showCategory = () => {
  const Modal = document.getElementById("categoriesModel");
  Modal.classList.toggle("hidden");
  Modal.classList.toggle("no-hidden");
};

const handleNameAndCategory = () => {
  filters.value["category__sub_category_name"] = "";
  filters.value["product_name__icontains"] = nameOfProduct.value;
  filters.value["category__category__category_name"] = store.state.selectedCategoryName;
  store.dispatch("fetchProducts");
};

defineComponent({
  components: {
    CategoryButton,
    CategoryDropDown,
    CategoryModal,
  },
});
</script>

<style scoped>
.bg-blue {
  --bg-opacity: 1;
  background-color: rgba(0, 178, 201, var(--bg-opacity));
}

.p-ab {
  position: absolute;
}

.text-white {
  color: white;
}

.bg-smoke {
  --bg-opacity: 1;
  background-color: rgba(242, 242, 242, var(--bg-opacity));
}

.main-search-container {
  padding: 12px;
  padding-top: 14px;
  width: 1300px;
  height: 80px;
}

.round-border {
  border-radius: 0.5rem;
}

.full-rounded-border {
  border-radius: 9999px;
}

.no-border {
  border: none;
}

.hidden {
  display: none;
}

.no-hidden {
  display: block;
  margin-top: 80px;
}

.no-outline {
  outline: none;
}

.white-bg {
  background-color: white;
}

span {
  opacity: 0.5;
  font-size: 18px;
  margin-bottom: 2px;
}

input {
  width: 650px;
}
</style>
