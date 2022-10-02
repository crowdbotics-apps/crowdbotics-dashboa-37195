from django.conf import settings
from django.db import models


class Plan(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=20,
    )
    description = models.TextField()
    price = models.DecimalField(
        max_digits=30,
        decimal_places=10,
    )
    created_at = models.DateTimeField(
        auto_now=True,
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
    )


class Subscription(models.Model):
    "Generated Model"
    active = models.BooleanField()
    created_at = models.DateTimeField(
        auto_now=True,
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
    )
    plan = models.ForeignKey(
        "subscriptions.Plan",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subscription_plan",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subscription_user",
    )
    app = models.ForeignKey(
        "app.Application",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subscription_app",
    )


# Create your models here.
