from django.contrib import admin
from app.models import User,Task
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdminModel(BaseUserAdmin):

    # The fields to be used in displaying the User Model model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["id","email","name","tc","is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        ('User Credentials', {"fields": ["email", "password",]}),
        ("Personal info", {"fields": ["name","tc",]}),
        ("Permissions", {"fields": ["is_admin",]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email","name","tc", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email","id"]
    filter_horizontal = []


# register the new UserAdmin
admin.site.register(User, UserAdminModel)
admin.site.register(Task)



