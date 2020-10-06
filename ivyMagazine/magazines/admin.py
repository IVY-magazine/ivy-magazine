import json

from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models.functions import TruncDay
# Register your models here.

from .models import *

admin.site.register(Customer)
admin.site.register(Magazine)
admin.site.register(Portfolio)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "data_created")
    ordering = ("-data_created",)

    def changelist_view(self, request, extra_context=None):
        # Aggregate new subscribers per day
        chart_data = (
            Customer.objects.annotate(date=TruncDay("data_created"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date")
        )

        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)