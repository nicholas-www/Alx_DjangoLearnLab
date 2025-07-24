from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year', 'author')
    search_fields = ('title', 'author')


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Fields shown in the user list view
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_active")
    list_filter = ("is_staff", "is_superuser", "is_active")

    # The fieldsets organize the admin form when editing a user
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "date_of_birth", "profile_photo")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    # Fields used when creating a new user in the admin
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "date_of_birth", "profile_photo", "is_staff", "is_active"),
        }),
    )

    search_fields = ("username", "email")
    ordering = ("username",)

# Register the model and custom admin
admin.site.register(CustomUser, CustomUserAdmin)