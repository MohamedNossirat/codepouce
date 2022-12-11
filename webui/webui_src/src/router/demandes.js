
export const demandesRouter = [
  {
    path: '/demandes',
    component: () => import('@/views/demandes/DemandeMainView'),
    children: [
      {
        path: ':id/:slug',
        name: 'DemandeView',
        component: () => import('@/views/demandes/nested/DemandeView'),
        props: true
      }
    ]
  }
]
