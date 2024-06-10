<template>
  <div class="container">
    <h2 class="color-b">Category<span v-if="product.category" class="color-b">
        /{{ product.category.sub_category_name }}
      </span>/ {{ product.product_name }}</h2>
  </div>

  <div class="container d-flex justify-content-between my-4">
    <div class="d-flex">
      <div class="py-2 px-2">
        <div v-for="image in product.product_image" class="py-1">
          <img :src=image alt="" height="70px" width="80px" @click="handleDisplayImage(image)">
        </div>
      </div>
      <div class="py-2 px-2">
        <img :src="imageOnDisplay" alt="" height="300px" width="400px">
      </div>
    </div>

    <div class="px-5 py-2">
      <div class="pb-4">
        <h3> {{ product.product_name }} </h3>
        <p> {{ product.short_description }} </p>
      </div>
      <div class="pb-5">
        <p> Brand: <span v-if="product.manufacturer"> {{ product.manufacturer.manufacturer_name }} </span></p>
        <p> Certifications: <span v-for="certificate in product.certifications"> {{ certificate.certification_name }},
          </span></p>
      </div>
      <div class="price-and-unit">
        <p style="font-size: 24px;"> $ {{ product.price }} / {{ product.unit }}</p>
      </div>



      <div class="py-1 text-center d-flex justify-content-around full-rounded-border">
        <button class="less-opacity no-border white-bg" @click="decrease" id="addBtn">
          <i class="fa">&#xf068;</i>
        </button>
        <div>
          {{ qunatity_to_display }}
        </div>
        <button class="no-border white-bg" @click="increase">
          <i class="fa fa-plus"></i>
        </button>
      </div>
    </div>
    <div>
      <div class="pb-3 d-flex">
        <img src="https://thebuyhive.com/buy/img/value1.c6cf714a.svg" alt="" height="40px" width="40px"
          class="mx-3 my-2">
        <div>
          <span style="color: black; text-wrap:wrap; text-align:justify;">Qualified and Verified Manufacturers</span>
        </div>
      </div>
      <div class="pb-3 d-flex">
        <img src="https://thebuyhive.com/buy/img/value2.e77aed11.svg" alt="" height="40px" width="40px"
          class="mx-3 my-1">
        <div>
          <span style="color: black;">Transparent Platform fees</span>
        </div>

      </div>
      <div class="pb-3 d-flex">
        <img src="	https://thebuyhive.com/buy/img/value3.71166266.svg" alt="" height="40px" width="40px" class="mx-3">
        <div class="mt-2">
          <span style="color: black;">Secure Payment</span>
        </div>
      </div>
      <div class="pb-3 d-flex">
        <img src="https://thebuyhive.com/buy/img/value4.2b9f535a.svg" alt="" height="40px" width="40px"
          class="mx-3 my-1">
        <div>
          <span style="color: black;">End to End B2B Sourcing</span>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const product = ref([])
const imageOnDisplay = ref('')
const qunatity_to_display = ref(0)

const route = useRoute()
const router = useRouter()

const handleDisplayImage = (url) => {
  imageOnDisplay.value = url
}

onMounted(async () => {
  try {
    const response = await axios.get(process.env.VUE_APP_ROOT_API + route.params.id);
    product.value = response.data;
    imageOnDisplay.value = product.value.product_image[0];
    qunatity_to_display.value = response.data.minimum_order_qunatity;
  } catch (error) {
    console.log(error.message);
    router.push({ name: 'ErrorMessage' });
  }
})
</script>

<style scoped>
i {
  font-size: 14px;
}
.color-b
{
  color: black;
}
.white-bg {
  background-color: white;
}

span {
  color: #00B2C9;
}

.full-rounded-border {
  border-radius: 9999px;
  border-width: 1px;
  border-style: solid;
  border-color: gray;
  width: 40%;
}

.no-border {
  border: none;
}

h3 {
  font-size: 36px;
}

p {
  font-size: 16px;
}

h2 {
  opacity: .5;
  font-size: 20px;
}

.less-opacity {
  opacity: .5;
}

.price-and-unit p {
  font-size: 24px;
}
</style>
