from django.contrib import admin
from .models import Plan, Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        query = super(SubscriptionAdmin, self).get_queryset(request)
        return query.filter(active=True)


admin.site.register(Plan)
admin.site.register(Subscription, SubscriptionAdmin)
