export default {
  namespaced: true,
  state: {
    local: null,
  },
  actions: {
    initializeLocal({commit}) {
      const local = localStorage.getItem('userLocal');
      if (!local) return
      commit('setLocal', local)
    }
  },
  mutations: {
    setLocal(state, local) {
      state.local = local
      localStorage.setItem('userLocal', local)
    },

  },
  getters: {}
}
