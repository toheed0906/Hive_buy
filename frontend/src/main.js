import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createStore } from "vuex";
import axios from 'axios';
const store = createStore({
    state: {
        categoryUrl: 'http://127.0.0.1:8000/categories/',
        products: [],
        categories: [],
        totalProducts: 0,
        filters:{
            min_price: '',
            max_price: '',
            stock_in_usa: '',
            minimimum_order_quantity: '',
            category__category__category_name: '',
            category__sub_category_name: '',
            product_name__icontains: '',
            manufacturer__location__in: '',
            ordering: '',
            page: 1,

        },
        selectedValue: 'Relevance',
        selctedCategoryName: " ",
        country_options: [
            { id: 1, name: "Hong Kong S.A.R", selected: false },
            { id: 2, name: "India", selected: false },
            { id: 3, name: "China", selected: false },
            { id: 4, name: "Vietnam", selected: false },
            { id: 5, name: "United States", selected: false },
            { id: 6, name: "Canada", selected: false },
            { id: 7, name: "Australia", selected: false },
            { id: 8, name: "United Kingdom", selected: false },
            { id: 9, name: "Korea, Republic of", selected: false },
        ],
        ordering_options: [
            { id: 1, name: "Relevance", ordering_param: '' },
            { id: 2, name: "Latest", ordering_param: 'created_at' },
            { id: 3, name: "Price Low To High", ordering_param: 'price' },
            { id: 4, name: "Price High To Low", ordering_param: '-price' },
            { id: 5, name: "MOQ Low To High", ordering_param: 'minimum_order_qunatity' },
            { id: 5, name: "Ratings High To Low", ordering_param: '-supplier__rating' },
          ],
        availableInUsa: false
    },

    getters: {
      minPrice: state => state.filters.min_price,
      maxPrice: state => state.filters.max_price,
      inUSA: state => state.availableInUsa,
      getProducts: state => state.products,
      getCategories: state => state.categories,
      getSelectedCountryName: state => state.selctedCategoryName,
    },

    actions: {
        async fetchProducts({ state, commit }) {
          try {
            const response = await axios.get(process.env.VUE_APP_ROOT_API, {params: state.filters});
            commit('setProducts', response.data.results);
            commit('setTotalProducts', response.data.count);
          } catch (error) {
            console.error(error);
            router.push({ name: "ErrorMessage" });
          }
        }
      },
      mutations: {
        setProducts(state, products) {
          state.products = products;
        },
        setTotalProducts(state,totalProducts)
        {
            state.totalProducts = totalProducts;
        },
        setMinPrice(state, newValue) {
          state.filters.min_price = newValue;
        },
        setMaxPrice(state, newValue) {
          state.filters.max_price = newValue;
        },
        setMinimumOrderQuantity(state, newValue)
        {
          state.filters.minimimum_order_quantity = newValue;
        },
        setAvailibityInUsa(state, newValue)
        {
          state.filters.stock_in_usa = newValue;
        },
        setManufacturerLocation(state, newValue)
        {
          state.filters.manufacturer__location__in = newValue;
        },
        setCategories(state, newValue)
        {
          state.categories = newValue
        },
        setCategoryAndSubCategory(state, newValue)
        {
          state.filters.category__category__category_name = newValue.cat
          state.filters.category__sub_category_name = newValue.subcat
        }
      }
   
})



createApp(App).use(router).use(store).mount('#app')

 