from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import User
from .forms import RegisterForm, LoginForm

class UserAdmin(BaseUserAdmin):
    add_form = RegisterForm

    list_display = ['email', 'admin', 'staff', 'active']
    list_filter = ['admin', 'staff', 'active']

    fieldsets = (
        ('Auth Info', {'fields': ('email', 'password',)}),
        ('Permissions', {'fields': ('admin', 'staff', 'active',)})
    )

    search_fields = ['email']
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)