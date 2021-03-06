from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('dashboard', views.DashboardView.as_view(), name='dashboard'),
    path('privacy', views.PrivacyView.as_view(), name='privacy'),
]