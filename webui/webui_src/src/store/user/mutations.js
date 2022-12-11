export default {
  initialize(state) {
    const token = localStorage.getItem('token');
    if (token) {
      state.token = token
      state.isAuthenticated = true
    } else {
      state.token = null
      state.isAuthenticated = false
    }
  },
  setToken(state, token) {
    state.token = token
    state.isAuthenticated = true
  },
  removeToken(state) {
    state.token = null
    state.isAuthenticated = false
  },
  setUser(state, user) {
    state.authUser = user
  }
}
