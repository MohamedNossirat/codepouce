import {createStore} from "vuex";
import user from "@/store/user";
import locale from "@/store/locale";
import demandes from "@/store/demandes";

const store = createStore({
  modules: {
    user,
    locale,
    demandes,
  }
})

export default store;
