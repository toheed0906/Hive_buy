import { createStore } from 'vuex'
import state from '@/store/state.js'
import getters from '@/store/getters.js'
import actions from '@/store/actions.js'
import mutations from '@/store/mutations.js'

export default createStore({
  state,
  getters,
  actions,
  mutations
})