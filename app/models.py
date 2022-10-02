from django.conf import settings
from django.db import models


class Application(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=50,
    )
    description = models.TextField()
    type = models.CharField(
        max_length=256,
    )
    framework = models.CharField(
        max_length=256,
    )
    domain_name = models.CharField(
        max_length=50,
    )
    screenshot = models.URLField()
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="application_user",
    )
    created_at = models.DateTimeField(
        auto_now=True,
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
    )


# Create your models here.
