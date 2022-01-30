from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from . import models

class HomeView(TemplateView):
    template_name = "index.html"


class DashboardView(PermissionRequiredMixin, TemplateView):
    template_name = "dashboard.html"
    permission_required = "dashboard.view_dashboard"
    login_url = 'request-access'
    raise_exception = False

class RequestAccessView(TemplateView):
    template_name = "request_access.html"