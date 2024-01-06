from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    list_display = ["email", "first_name", "last_name", "last_login", "date_joined", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["first_name", "last_name", "phone_number"]}),
        ("Permissions", {"fields": ["is_active", "is_admin", "is_staff", "is_superuser"]}),
    ]
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',"first_name", "last_name", 'is_active', 'is_admin', 'is_staff', 'is_superuser'),
        }),
    )
    readonly_fields = ["last_login","date_joined"]
    search_fields = ["email"]
    ordering = ["-date_joined","email"]
    filter_horizontal = []

admin.site.register(Account, AccountAdmin)
