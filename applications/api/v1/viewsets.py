from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated

from applications.api.v1.serializers import AppSerializer
from applications.models import App
from home.permissions import OwnerPermission
from rest_framework import viewsets


class AppViewSet(viewsets.ModelViewSet):
    serializer_class = AppSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = App.objects.all()
    permission_classes = (IsAuthenticated, OwnerPermission)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
