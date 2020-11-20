import json

from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db.models.functions import TruncDay

from .models import *

admin.site.register(Customer)

@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = ("name", "date_created", "viewcount")
    ordering = ("-date_created",)

    def changelist_view(self, request, extra_context=None):
        # each column data of name, viewcount, and magazineGroup in Magazine objects
        magazine_data = (
            Magazine.objects.values('name', 'viewcount', 'magazineGroup')
        )

        # each column data of username and groups in User objects
        user_groups_data = (
            list(User.objects.values_list('username','groups'))
         )

        # each column data of id and name in Group objects
        groups_data = (
            list(Group.objects.values('id', 'name'))
         )

        # Serialize and attach the chart data to the template context
        as_json_magazine = json.dumps(list(magazine_data), cls=DjangoJSONEncoder)
        as_json_user = json.dumps(list(user_groups_data), cls=DjangoJSONEncoder)
        as_json_groups = json.dumps(list(groups_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"magazine_data": as_json_magazine, "user_groups_data": as_json_user, "groups_data": as_json_groups}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "data_created")
    ordering = ("-date_created",)

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

class PostImageAdmin(admin.StackedInline):
    model = PostImage


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "date_created", "viewcount") 
    ordering = ("-date_created",)

    def changelist_view(self, request, extra_context=None):

        # each column data of title and viewcount in Post objects
        chart_data = (
            Post.objects.values('title', 'viewcount')
        )

        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)
    inlines = [PostImageAdmin]

    class Meta:
       model = Post

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass