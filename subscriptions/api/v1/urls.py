from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import PlanViewSet, SubscriptionViewSet, AppSubscriptionViewSet

router = DefaultRouter()
router.register("plan", PlanViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        'subscription/<int:app_id>/',
        AppSubscriptionViewSet.as_view({"get": "list",
                                        "patch": "update", "delete": "destroy"}),
        name='app_subscription',
    )
]
