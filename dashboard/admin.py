from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import DashboardUser

admin.site.register(DashboardUser, UserAdmin)