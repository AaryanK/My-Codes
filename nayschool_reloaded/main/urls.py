from django.urls import path,include
from main import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("",views.home ,name="home"),
    path("api/courses_info/",views.courses_info ,name="home"),
    ]
