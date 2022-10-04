from django.conf import settings
from django.db import models
from home.models import BaseModel


class App(BaseModel):
    """
    User applications
    """
    APP_TYPE_WEB = "Web"
    APP_TYPE_MOBILE = "Mobile"

    APP_TYPE_CHOICES = (
        (APP_TYPE_WEB, "Web"),
        (APP_TYPE_MOBILE, "Mobile"),
    )

    FRAMEWORK_DJANGO = "Django"
    FRAMEWORK_REACT_NATIVE = "React Native"
    FRAMEWORK_CHOICES = (
        (FRAMEWORK_DJANGO, "Django"),
        (FRAMEWORK_REACT_NATIVE, "React Native"),
    )
    name = models.CharField(
        max_length=50, unique=True
    )
    description = models.TextField()
    type = models.CharField(
        max_length=256, choices=APP_TYPE_CHOICES
    )
    framework = models.CharField(
        max_length=256, choices=FRAMEWORK_CHOICES
    )
    domain_name = models.CharField(
        max_length=253,
        blank=True,
        null=True
    )
    screenshot = models.URLField(blank=True, null=True)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="app_user",
    )

    def __str__(self):
        return self.name
