from django.urls import path, include
from .views import AccountViewSet

urlpatterns = [
    path('', include(
        [
            path('register/', AccountViewSet.as_view({'post': 'create'})),
            path('<int:pk>/update/', AccountViewSet.as_view({
                'get': 'retrieve',
                'put': 'update',
                'patch': 'partial_update',
            }), name='update-user'),
            path('<int:pk>/delete/', AccountViewSet.as_view({
                'delete': 'destroy'
            }), name='delete-user'),
            path('me/', AccountViewSet.as_view({'get': 'me'}))
        ]
    ))
]
