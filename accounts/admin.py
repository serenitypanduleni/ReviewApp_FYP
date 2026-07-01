from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserModel


class UserModelAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "phone_number", "is_number_verified", "user_role")

admin.site.register(UserModel, UserModelAdmin)
