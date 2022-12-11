from rest_framework import viewsets
from .serializers import UserSerializer, UserMeSerializer
from .models import CodePouceUser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import PermissionPolicyMixin


class AccountViewSet(PermissionPolicyMixin, viewsets.ModelViewSet):
    queryset = CodePouceUser.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes_per_method = {
        "list": [IsAuthenticated],
        "create": [AllowAny],
        "retrieve": [IsAuthenticated],
        "update": [IsAuthenticated],
        "destroy": [IsAuthenticated],
        "partial_update": [IsAuthenticated],
        'me': [IsAuthenticated]
    }

    @action(detail=False)
    def me(self, request):
        return Response(UserMeSerializer(self.request.user).data)
