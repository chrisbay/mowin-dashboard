from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('request-access', views.RequestAccessView.as_view(), name='request-access'),
    path('dashboard', views.DashboardView.as_view(), name='dashboard'),
]