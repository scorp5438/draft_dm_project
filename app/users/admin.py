from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


# from users.forms import CustomUserChangeForm


# admin.site.register(User)


class CustomUserAdmin(UserAdmin):
    model = User
    # form = CustomUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('company', 'post')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('company', 'post')}),
    )
    list_display = ['username', 'is_staff', 'company', 'post']


admin.site.register(User, CustomUserAdmin)
