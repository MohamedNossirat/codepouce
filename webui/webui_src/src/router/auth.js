import AuthView from "@/views/auth/AuthView";

export const authRoutes = [
  {
    path: '/auth',
    component: AuthView,
    children: [
      {
        path: 'login',
        name: 'Login',
        component: () => import('@/views/auth/nested/LoginView')
      },
      {
        path: 'reset_password',
        name: 'ResetPassword',
        component: () => import('@/views/auth/nested/ResetPasswordView'),
      },
      {
        path: 'reset_password_confirm/:uid/:token',
        name: 'ResetPasswordConfirm',
        component: () => import('@/views/auth/nested/ResetPasswordConfirmView')
      },
      {
        path: 'signup',
        name: 'Signup',
        component: () => import('@/views/auth/nested/SignupView')
      }
    ]
  }
]
