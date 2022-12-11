import {createRouter, createWebHashHistory} from "vue-router";
import store from "@/store";
import {appRoutes} from './app'
import {authRoutes} from "@/router/auth";
import {demandesRouter} from "@/router/demandes";

const routes = [
  ...appRoutes,
  ...authRoutes,
  ...demandesRouter,
]

const codePouceRouter = createRouter({
  history: createWebHashHistory(),
  routes
})
codePouceRouter.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.user.isAuthenticated) next('/auth/login')
  else next()
})
export default codePouceRouter;
