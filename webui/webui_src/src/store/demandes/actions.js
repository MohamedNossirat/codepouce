import httpClient from "@/http/httpClient";

export default {
  async getDemandes({commit, state}) {
    if (isNaN(state.params.next) || state.params.next === undefined) return;
    let params = {
      page: state.params.next
    }
    const res = await httpClient.get('api/demandes/', {params: params});
    if (!res) return;
    commit('setDemandes', res)
  }
}
