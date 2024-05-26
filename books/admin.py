"""registration of models to django admin web gui"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(DefaultUserAdmin):
    """custom user class"""

    list_display = DefaultUserAdmin.list_display + (
        "profile_picture_url",
        "bio",
    )
    fieldsets = DefaultUserAdmin.fieldsets + (
        ("Additional Information", {"fields": ("profile_picture_url", "bio")}),
    )

    readonly_fields = (
        "date_joined",
        "last_login",
        "username",
    )
