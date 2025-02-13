from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import CreateUserForm, UpdateUserForm


class MyUserAdmin(UserAdmin):
    add_form = CreateUserForm
    form = UpdateUserForm
    model = User
    list_display = ['email', 'username', 'avatar', 'created', 'karma', 'about', 'verified']
    fieldsets = [
        (None, {"fields": ["email", 'username', 'verified', "password"]}),
        ("Personal info", {"fields": ["about"]}),
        ("Permissions", {"fields": ["is_active", "is_staff", "is_superuser"]})
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "username", "password1", "password2", 'about', 'verified', 'avatar', 'is_staff'],
            },
        ),
    ]
    search_fields = ["email", 'username']
    ordering = ["created"]
    filter_horizontal = []


admin.site.register(User, MyUserAdmin)
