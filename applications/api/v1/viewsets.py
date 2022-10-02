from rest_framework import authentication
from applications.models import App
from .serializers import AppSerializer
from rest_framework import viewsets


class AppViewSet(viewsets.ModelViewSet):
    serializer_class = AppSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = App.objects.all()
