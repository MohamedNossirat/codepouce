import {createStore} from "vuex";
import user from "@/store/user";
import local from "@/store/local";
import demandes from "@/store/demandes";

const store = createStore({
  modules: {
    user,
    local,
    demandes,
  }
})

export default store;
