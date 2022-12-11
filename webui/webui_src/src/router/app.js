export const appRoutes = [
  {
    path: '/',
    component: () => import('@/views/app/AppView'),
    meta: {
      requireLogin: true
    },
    children: [
      {
        path: '',
        name: 'HomePage',
        component: () => import('@/views/app/nested/HomeView')
      }
    ]
  },

]
