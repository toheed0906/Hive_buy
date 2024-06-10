import { createRouter, createWebHistory } from 'vue-router'
import ProductView from '../views/ProductView.vue'
import ProductDetailView from '../views/ProductDetailView.vue'
import ErrorMessage from '@/views/ErrorMessage.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: ProductView
  },
  { path: '/product/:id', 
    name: 'productsdetail',
    component: ProductDetailView
  },
  {
    path: '/error/',
    name: 'ErrorMessage',
    component: ErrorMessage
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
