from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from . import models

class HomeView(TemplateView):
    template_name = "index.jinja"


class DashboardView(PermissionRequiredMixin, TemplateView):
    template_name = "dashboard.jinja"
    permission_required = "dashboard.view_dashboard"
    login_url = 'request-access'
    raise_exception = False

class RequestAccessView(TemplateView):
    template_name = "request_access.jinja"