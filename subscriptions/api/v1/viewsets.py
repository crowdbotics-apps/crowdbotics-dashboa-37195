from rest_framework import authentication, permissions, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response

from home.permissions import OwnerPermission
from subscriptions.models import Plan, Subscription
from .serializers import PlanSerializer, SubscriptionSerializer, AppSubscriptionSerializer
from rest_framework import viewsets


class ActionBasedPermission(AllowAny):
    """
    Grant or deny access to a view, based on a mapping in view.action_permissions
    """
    def has_permission(self, request, view):
        for klass, actions in getattr(view, 'action_permissions', {}).items():
            if view.action in actions:
                return klass().has_permission(request, view)
        return False


class PlanViewSet(viewsets.ModelViewSet):
    serializer_class = PlanSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    action_permissions = {
        IsAdminUser: ['update', 'partial_update', 'destroy', 'create'],
        IsAuthenticated: ['retrieve', 'list']
    }
    queryset = Plan.objects.all()
    permission_classes = (ActionBasedPermission,)
    paginator = None


class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Subscription.objects.all()

    permission_classes = (IsAuthenticated, OwnerPermission)


class AppSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = AppSubscriptionSerializer
    permission_classes = (IsAuthenticated, OwnerPermission)

    def get_object(self):
        return Subscription.objects.get(app__id=self.kwargs['app_id'])

    def list(self, request, *args, **kwargs):
        subscription = self.get_object()
        serializer = self.get_serializer(subscription)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        plan_id = request.data.pop("plan")
        plan = Plan.objects.get(name="Free")
        try:
            plan = Plan.objects.get(id=plan_id)
        except Plan.DoesNotExist:
            pass

        subscription = self.get_object()
        subscription.plan = plan
        subscription.save(update_fields=["plan"])
        serializer = self.get_serializer(subscription)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
