from rest_framework import viewsets
from .models import Demande
from .serializers import DemandeSerailizers
from .paginations import CodePouceDemandePagination
from .permissions import PermissionPolicyMixin
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import action


class DemandeViewSet(PermissionPolicyMixin, viewsets.ModelViewSet):
    queryset = Demande.objects.all().order_by('-created')
    serializer_class = DemandeSerailizers
    pagination_class = CodePouceDemandePagination
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    permission_classes_per_method = {
        "list": [permissions.IsAuthenticated],
        "create": [permissions.IsAuthenticated],
        "retrieve": [permissions.IsAuthenticated],
        "update": [permissions.IsAuthenticated],
        "destroy": [permissions.IsAuthenticated],
        "partial_update": [permissions.IsAuthenticated],
    }

    @action(detail=False)
    def delete_all(self, request):
        Demande.objects.all().delete()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
