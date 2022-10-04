from rest_framework import serializers
from applications.api.v1.serializers import AppSerializer
from subscriptions.models import Plan, Subscription


class PlanSerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    price = serializers.DecimalField(required=False, max_digits=10, decimal_places=2)

    class Meta:
        model = Plan
        exclude = ("created_at", "updated_at")


class SubscriptionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    plan = PlanSerializer(required=True)
    app = AppSerializer(required=True)

    class Meta:
        model = Subscription
        exclude = ("created_at", "updated_at")


class AppSubscriptionSerializer(serializers.ModelSerializer):
    plan = PlanSerializer()

    class Meta:
        model = Subscription
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.plan = validated_data.get('plan', instance.plan)
        instance.save()
        return instance
