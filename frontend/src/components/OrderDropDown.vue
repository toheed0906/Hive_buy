<template>
    <div class="dropdown">
        <button class="btn btn-secondary dropdown-border no-border no-outline py-2 px-2" type="button"
            id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            {{ store.state.selectedValue }}

            <img src="https://thebuyhive.com/buy/img/chevronDown.e08abe09.svg">
        </button>

        <div class="dropdown-menu menu" aria-labelledby="dropdownMenuButton">
            <a class="dropdown-item" href="#" v-for="option in store.state.ordering_options" :key="option.id"
                @click="handleOrdering(option.name, option.ordering_param)">{{ option.name }}</a>
        </div>
    </div>
</template>

<script setup>
import { useStore } from 'vuex';
const store = useStore()
const handleOrdering = (name, ordering_param) => {
    store.state.selectedValue = name;
    store.state.filters['ordering'] = ordering_param
    store.dispatch('fetchProducts')
};
</script>

<style scoped>
.product-banner {
    padding-right: 160px;
    padding-bottom: 20px;
}

.no-border {
    border: none;
}

.no-outline {
    outline: none;
}

img {
    padding-left: 20px;
    padding-bottom: 4px;
}

.dropdown-border {
    border-radius: 9999px;
    border-width: 1px;
    border-color: rgba(35, 31, 32, .15);
    --bg-opacity: 1;
    background-color: rgba(242, 242, 242, var(--bg-opacity));
    color: black;
    width: 220px;
    padding: 4px;
    margin-bottom: 4px;
}

.item:hover {
    .hidden {
        display: block;
    }

    .hover-box-shadow {
        box-shadow: 0 2px 12px -5px #231f20;
    }

}

.dropdown:hover>.dropdown-menu {
    display: block;
    box-shadow: none;
}

.dropdown>.dropdown-toggle:active {
    pointer-events: none;
}


.menu {
    width: 220px;
}
</style>