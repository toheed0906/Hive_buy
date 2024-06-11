export default {
    setProducts(state, response) {
      state.products = response.results;
      state.totalProducts = response.count;
    },
    setMinPrice(state, newValue) {
      state.filters.min_price = newValue;
    },
    setMaxPrice(state, newValue) {
      state.filters.max_price = newValue;
    },
    setMinimumOrderQuantity(state, newValue) {
      state.filters.minimum_order_qunatity = newValue;
    },
    setAvailibityInUsa(state, newValue) {
      state.filters.stock_in_usa = newValue;
    },
    setManufacturerLocation(state, newValue) {
      state.filters.manufacturer__location__in = newValue;
    },
    setCategories(state, newValue) {
      state.categories = newValue
    },
    setCategoryAndSubCategory(state, newValue) {
      state.filters.category__category__category_name = newValue.cat
      state.filters.category__sub_category_name = newValue.subcat
    }
  }