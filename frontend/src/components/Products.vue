<template>
    <div class="container py-5 left-mar" >
        <div class="row">
            <div v-for="item in store.state.products" class="col-12 col-sm-6 col-md-4 col-lg-4 item mb-4">
                <div class="card hover-box-shadow h-100 no-border sizing" 
                    @click="$router.push(`/product/${item.id}`)">
                    <div class="d-flex justify-content-center no-border">
                        <img :src="item.product_image[0]" height="40px" width="200px" class="img-fluid">
                    </div>
                    <div class="card-body px-3" >
                        <p class="product-name">{{ item.product_name }}</p>
                        <p class="qunatity"> MOQ: {{ item.minimum_order_qunatity }} {{ item.unit }}</p>
                        <div class="detail-box-price"> $ {{ item.price }}.00 / {{ item.unit }}</div>
                        <div>
                            <button class="w-full bg-blue text-white py-1 d-block">
                                Add To Chart
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script setup>
import { useStore } from 'vuex';
const store = useStore();


</script>


<style scoped>
.no-border {
    border: none;
}
.sizing
{
    width: 300px;
    height: 40px;
}

.rounded-full {
    border-width: 9999px;
    border-radius: 1px;
    --border-opacity: 1;
    border-color: rgba(200, 199, 199, var(--border-opacity));
    --bg-opacity: 1;
    background-color: rgba(255, 255, 255, var(--bg-opacity));
}
.left-mar
{
    margin-left: 22px;
}
.bg-smoke {
    --bg-opacity: 1;
    background-color: rgba(242, 242, 242, var(--bg-opacity));
    padding: 10px 20px;
}

.white-bg {
    background-color: white;
    border-radius: 9999px;
    padding: 12px 20px;
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

.product-name {
    text-transform: capitalize;
    overflow: hidden;
    width: 100%;
    text-overflow: ellipsis;
    white-space: nowrap;
    font: 18px;
    margin: 0;
}

.product-banner {
    padding-right: 160px;
    padding-bottom: 20px;
}

.qunatity {
    margin: 0;
    opacity: .5;
    padding-top: 4px;
}

.detail-box-price {
    letter-spacing: -.05em;
    font-size: 18px;
    font-weight: 600;
    overflow: hidden;
    width: 100%;
    text-overflow: ellipsis;
    padding-top: 4px;
}

.text-white {
    --text-opacity: 1;
    color: #fff;
    color: rgba(255, 255, 255, var(--text-opacity));
}

.hidden {
    display: none;
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

.title {
    font-size: 18px;
    opacity: .5;
    padding-left: 120px;
}

.main-content:has(input#modal-toggle:checked) {
    visibility: hidden;
}

/* Show modal when open */
body:has(input#modal-toggle:checked) .modal {
    display: block;
}

.w-full {
    width: 100%;
    border-radius: .5rem;
    border: none;
}

.bg-blue {
    --bg-opacity: 1;
    background-color: #00b2c9;
    background-color: rgba(0, 178, 201, var(--bg-opacity));
}
img
{
    border-radius: 1%; 
    padding-top: 20px;
}
h3 {
    font-size: 1.125rem;
    color: #231f20;
    padding-bottom: 12px;
}

.input-container {
    padding-top: 32px;
}

.see-more-link {
    text-decoration: underline;
    color: #29b574;
    cursor: pointer;
    margin-bottom: 0;
}

.menu {
    width: 220px;
}
</style>