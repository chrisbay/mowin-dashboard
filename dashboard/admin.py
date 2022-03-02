from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import DashboardUser

class DashboardUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_joined')
    list_filter = ('groups', 'date_joined')

admin.site.register(DashboardUser, DashboardUserAdmin)