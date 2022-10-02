from rest_framework import serializers
from applications.models import App


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = "__all__"
