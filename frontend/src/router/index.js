import { createRouter, createWebHistory } from 'vue-router'
import appRoutes from '@/router/routes.js'

const routes = [
  ...appRoutes,
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
