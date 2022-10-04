from django.utils.html import escape
from rest_framework import serializers
from applications.models import App
from subscriptions.models import Subscription, Plan


class AppSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    domain_name = serializers.CharField(required=False)
    type = serializers.CharField(required=False)
    framework = serializers.CharField(required=False)
    screenshot = serializers.URLField(required=False)
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    def create(self, validated_data):
        request = self.context.get("request")
        app = App.objects.create(**validated_data)
        plan = Plan.objects.get(name="Free")
        Subscription.objects.create(
            app=app,
            plan=plan,
            user=request.user
        )
        return app

    def validate_name(self, value):
        return escape(value)

    def validate_description(self, value):
        return escape(value)

    def validate_domain_name(self, value):
        return escape(value)

    def validate_type(self, value):
        return escape(value)

    def validate_framework(self, value):
        return escape(value)

    class Meta:
        model = App
        exclude = ("created_at", "updated_at")
