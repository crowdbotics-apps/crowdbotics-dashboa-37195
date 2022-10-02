from rest_framework import authentication
from users.models import UserDetails
from .serializers import UserDetailsSerializer
from rest_framework import viewsets


class UserDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = UserDetailsSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = UserDetails.objects.all()
