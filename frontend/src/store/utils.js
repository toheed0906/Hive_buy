export function getFilters(filters) {
    let validFilters = {}
    for (let item in filters) {
      if (filters[item]) {
        validFilters[item] = filters[item]
      }
    }
    return validFilters
  }