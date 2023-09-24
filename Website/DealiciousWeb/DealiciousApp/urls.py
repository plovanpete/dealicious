from django.urls import path
from . import views

urlpatterns = [
    path('', views.DealiciousView, name='home'),
    path('Report/', views.ReportView, name='report'),
]
