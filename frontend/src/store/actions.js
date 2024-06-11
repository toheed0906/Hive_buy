import axios from 'axios'
import { getFilters } from '@/store/utils.js';
import router from '@/router/index.js';
import { HTTP } from '@/request.js';

export default {
  async fetchProducts({ state, commit }) {
    try {
      const response = await HTTP.get('/products/', { params: getFilters(state.filters) });
      commit('setProducts', response.data);
    } catch (error) {
      console.error(error);
      router.push({ name: "error-message" });
    }
  }
}