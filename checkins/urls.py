from django.urls import path
from . import views

app_name = "checkins"
urlpatterns = [
    path('', views.home, name='checkins-home'),
    path('checkins/<pk>/', views.checkin_detail, name='checkins-detail'),
]