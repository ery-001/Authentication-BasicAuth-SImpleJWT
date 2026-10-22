from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    ordering = ("email",)
    list_display = ("email", "username", "is_active", "is_verified", "is_staff")
    fieldsets = DjangoUserAdmin.fieldsets + (
        ("Verification", {"fields": ("is_verified",)}),
    )
