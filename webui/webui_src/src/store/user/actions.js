import httpClient from "@/http/httpClient";

export default {
  initializeStore({commit}) {
    commit('initialize');
  },
  async login({commit}, {email, password}) {
    httpClient.defaults.headers.common['Authorization'] = '';
    localStorage.removeItem('token');
    commit('removeToken');
    const res = await httpClient.post('api/auth/token/login/', {email, password});
    if (res) {
      commit('setToken', res.data.auth_token)
      httpClient.defaults.headers.common['Authorization'] = 'Token ' + res.data.auth_token;
      localStorage.setItem('token', res.data.auth_token);
    }
  },
  async logout({commit}) {
    const res = await httpClient.post('api/auth/token/logout/')
    if (res) {
      httpClient.defaults.headers.common['Authorization'] = '';
      localStorage.removeItem('token');
      commit('removeToken');
    }
  },
  async signup({commit}, signUpObject) {
    httpClient.defaults.headers.common['Authorization'] = null;
    if (!signUpObject) return
    const formDate = new FormData();
    Object.keys(signUpObject).forEach((key) => {
      if (key === 'langues') {
        formDate.append(key, JSON.stringify(signUpObject[key]));
      } else {
        formDate.append(key, signUpObject[key])
      }
    })
    const res = httpClient.post('api/account/register/', formDate);
    if (res) {
      console.log(res);
    }
  },
  async sendResetPasswordRequest({commit}, email) {
    httpClient.defaults.headers.common['Authorization'] = '';
    localStorage.removeItem('token');
    return await httpClient.post('api/auth/users/reset_password/', {email})
  },
  async resetPasswordConfirm({}, resetpasswordObject) {
    httpClient.defaults.headers.common['Authorization'] = '';
    localStorage.removeItem('token');
    return await httpClient.post('api/auth/users/reset_password_confirm/', resetpasswordObject)
  },
  async getUserMe({commit}) {
    const res = await httpClient.get('api/account/me/');
    if (res) {
      commit('setUser', res.data)
    }
  }

}
