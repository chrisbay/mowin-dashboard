from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "index.jinja"

class DashboardView(TemplateView):
    template_name = "dashboard.jinja"

class PrivacyView(TemplateView):
    template_name = "privacy.jinja"
