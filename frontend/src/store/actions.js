import axios from 'axios'
import { getFilters } from '@/store/utils.js';
import router from '@/router/index.js';
export default {
  async fetchProducts({ state, commit }) {
    try {
      const response = await axios.get(process.env.VUE_APP_ROOT_API + '/products/', { params: getFilters(state.filters) });
      commit('setProducts', response.data);
    } catch (error) {
      console.error(error);
      router.push({ name: "error-message" });
    }
  }
}