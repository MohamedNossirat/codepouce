from django.urls import path, include
from .views import DemandeViewSet

all_demandes = DemandeViewSet.as_view({'get': 'list'})
demande_create = DemandeViewSet.as_view({'post': 'create'})
demande_details = DemandeViewSet.as_view({'get': 'retrieve'})
demande_update = DemandeViewSet.as_view({'put': 'update'})
demande_delete = DemandeViewSet.as_view({'delete': 'destroy'})
demande_patch = DemandeViewSet.as_view({'patch': 'partial_update'})
delete_all = DemandeViewSet.as_view({'get': 'delete_all'})

urlpatterns = [
    path('', include([
        path('', all_demandes, name='all_demandes'),
        path('create/', demande_create, name='demande-create'),
        path('delete/', delete_all, name='demande-create'),
        path('<uuid:pk>/', demande_details, name='demande-details'),
        path('<uuid:pk>/update/', demande_update, name='demande-update'),
        path('<uuid:pk>/delete/', demande_delete, name='demande-delete'),
        path('<uuid:pk>/patch/', demande_patch, name='demande-patch'),
    ]))
]
