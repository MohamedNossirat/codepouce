import HomeView from "@/views/app/nested/HomeView";
import AppView from "@/views/app/AppView";

export const appRoutes = [
  {
    path: '/',
    component: AppView,
    meta: {
      requireLogin: true
    },
    children: [
      {
        path: '',
        name: 'HomePage',
        component: HomeView
      }
    ]
  },

]
