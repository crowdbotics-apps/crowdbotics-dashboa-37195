from django.conf import settings
from django.db import models
from django.db.models import QuerySet

from home.models import BaseModel


class Plan(BaseModel):
    """
    Pricing plan
    """
    name = models.CharField(
        max_length=20,
    )
    description = models.TextField()
    price = models.DecimalField(
        max_digits=30,
        decimal_places=10,
    )
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class CustomQuerySet(QuerySet):
    def delete(self):
        self.update(active=False)


class SubscriptionManager(models.Manager):
    def active(self):
        return self.model.objects.filter(active=True)

    def get_queryset(self):
        return CustomQuerySet(self.model, using=self._db)


class Subscription(BaseModel):
    """
    App subscriptions
    """
    active = models.BooleanField(default=True)
    plan = models.ForeignKey(
        "subscriptions.Plan",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="subscription_plan",
    )
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="subscription_user",
    )
    app = models.OneToOneField(
        "applications.App",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="subscription_app",
    )

    objects = SubscriptionManager()

    def delete(self, **kwargs):
        self.active = False
        self.save(update_fields=('active',))

    def __str__(self):
        return f"{self.user.username} - {self.plan.name} - {self.app.name}"
