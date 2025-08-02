from django.contrib import admin
from .models import Plan

def is_admin_user(user):
    return user.is_superuser or user.is_staff

class StaffPermissionPlanAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        return is_admin_user(request.user)

    def has_module_permission(self, request):
        return is_admin_user(request.user)

    def has_add_permission(self, request):
        return is_admin_user(request.user) 

    def has_change_permission(self, request, obj=None):
        return is_admin_user(request.user) 

    def has_delete_permission(self, request, obj=None):
        return is_admin_user(request.user) 

admin.site.register(Plan, StaffPermissionPlanAdmin)
