export default {
  setDemandes(state, payload) {
    payload.data.forEach(demande => {
      state.demandes.push(demande)
    });
    state.params = {
      ...state.params,
      current: parseInt(payload.headers.current),
      next: parseInt(payload.headers.next),
      previous: parseInt(payload.headers.previous),
      total: parseInt(payload.headers.total)
    }
  }
}
