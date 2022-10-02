from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import UserDetailsViewSet

router = DefaultRouter()
router.register("userdetails", UserDetailsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
