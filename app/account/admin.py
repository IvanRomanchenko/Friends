from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from import_export.admin import ImportExportMixin, ExportActionMixin

from account.templatetags.acc_extras import go_to_main_page
from .models import Profile, Note


# Change the admin icon
admin.site.site_header = go_to_main_page()

# Puts away the tables of Groups of the admin panel
admin.site.unregister(Group)


@admin.register(Profile)
class ProfileAdmin(ImportExportMixin, ExportActionMixin, UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_active')
    fieldsets = (
        (None, {
            'fields': ('username', 'password',)
        }),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name', 'birthday', 'biography',
                       'contacts', 'ip')
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',
                       'user_permissions'),
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined',)
        }),
    )
    actions = ('activate', 'deactivate',)

    @admin.display(description='Activate')
    def activate(self, request, queryset):
        queryset.update('is_active', True)

    @admin.display(description='Deactivate')
    def deactivate(self, request, queryset):
        queryset.update('is_active', False)

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return 'last_login', 'date_joined',
        return 'last_login', 'date_joined', 'is_superuser',


@admin.register(Note)
class NoteAdmin(ImportExportMixin, ExportActionMixin, admin.ModelAdmin):
    list_filter = ('signal_type',)
    search_fields = ('username',)
