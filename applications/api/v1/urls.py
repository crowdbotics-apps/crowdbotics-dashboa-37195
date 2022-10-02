from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AppViewSet

router = DefaultRouter()
router.register("app", AppViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
