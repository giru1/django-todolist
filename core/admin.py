from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core.models import User


# Register your models here.

class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'username')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    exclude = ('password',)
    readonly_fields = ('last_login', 'date_joined')

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if not obj:
            return fieldsets
        return [(name, {'fields': [f for f in fields if f != 'password']}) for name, fields in fieldsets]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)