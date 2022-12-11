import DemandeMainView from "@/views/demandes/DemandeMainView";
import DemandeView from "@/views/demandes/nested/DemandeView";

export const demandesRouter = [
  {
    path: '/demandes',
    component: DemandeMainView,
    children: [
      {
        path: ':id/:slug',
        name: 'DemandeView',
        component: DemandeView,
        props: true
      }
    ]
  }
]
