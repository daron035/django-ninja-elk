from django.contrib import admin

from core.apps.customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "phone", "created_at")
    list_display_links = ("id", "phone")
    search_fields = ("phone",)
