<template>
  <div>
    <div class="d-flex justify-content-center">
      <nav class="navbar navbar-expand-sm navbar-expand-lg navbar-light pt-3 pb-3 d-flex ">
        <div class="container no-left-padding">
          <a href="" @click="$router.push('/')">
            <img src="../assets/logo.png" alt="" width="200" height="70" >
          </a>

          <button class="navbar-toggler navbar-toggler-right" type="button" data-bs-toggle="collapse"
            data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>

          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
              <li v-for="item in navItems" class="nav-item nav-item-style">
                <a class="nav-link" href="#"> {{ item }}</a>
              </li>
            </ul>
          </div>


          <div class="d-flex justify-content-center">
            <div>
              <button class="d-flex justify-content-center rounded-pill border-blue py-1 px-4 bg-transparent"><span
                  class="text-blue">Register</span></button>
            </div>

            <div class="mrl-5">
              <button class="d-flex justify-content-center rounded-pill border-blue py-1 px-4 bg-transparent"><span
                  class="text-blue"> Login</span></button>
            </div>
          </div>
        </div>
      </nav>
    </div>
  </div>
</template>

<script setup>
import {ref} from 'vue';
const navItems = ref(['Expert Sourcing', 'Contract Manufacturing', 'Buy', 'Financing', 'About Us'])
</script>

<style scoped>
.nav-item-style {
  padding-right: 36px;
  padding-left: 36px;
  font-size: 14px;
  font-weight: bolder;
}

.nav-item-style a {
  color: #231f20;
}

.border {
  border-width: 1px;
}
.no-left-padding
{
  padding-left: 0;
}
.border-blue {
  --border-opacity: 1;
  border-color: rgba(0, 178, 201, var(--border-opacity));
}

.text-blue {
  --text-opacity: 1;
  color: #00b2c9;
  color: rgba(0, 178, 201, var(--text-opacity));
}
img
{
  margin-left: 0 ; 
  margin-right: 20px;
}
.mrl-5
{
  margin-left: 10px;
}
</style>