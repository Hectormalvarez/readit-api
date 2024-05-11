"""registration of models to django admin web gui"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(DefaultUserAdmin):
    """custom user class"""
