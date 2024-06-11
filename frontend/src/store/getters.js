export default {
    minPrice: state => state.filters.min_price,
    maxPrice: state => state.filters.max_price,
    inUSA: state => state.availableInUsa,
    getProducts: state => state.products,
    getCategories: state => state.categories,
    getSelectedCategoryName: state => state.selctedCategoryName,
    getCountryOptions: state => state.country_options,
    getFilters: state => state.filters,
  }