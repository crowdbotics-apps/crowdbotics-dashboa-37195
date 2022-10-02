from rest_framework import authentication
from app.models import Application
from .serializers import ApplicationSerializer
from rest_framework import viewsets


class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Application.objects.all()
