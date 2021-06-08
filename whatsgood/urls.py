
from django.contrib import admin
from django.urls import path, include
from checkins.views import home, checkin_detail

app_name = "whatsgood"
urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', include('checkins.urls')),
]
