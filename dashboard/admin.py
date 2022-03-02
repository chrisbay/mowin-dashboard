from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import DashboardUser
import pytz

class DashboardUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'date_joined', 'date_joined_cst')
    list_filter = ('groups', 'date_joined')

    @admin.display(description='Date Joined (CST)')
    def date_joined_cst(self, obj):
        return obj.date_joined.astimezone(pytz.timezone('US/Central')).strftime('%b %d, %Y')

admin.site.register(DashboardUser, DashboardUserAdmin)