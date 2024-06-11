export default [
    {
        path: '/', name: 'home',
        component: () => import('@/views/ProductView.vue') 
    },
    {
        path: '/product/:id', name: 'products-detail',
        component: () => import('@/views/ProductDetailView.vue')
    },
    {
        path: '/error/', name: 'error-message',
        component: () => import('@/views/ErrorMessage.vue')
    },
]