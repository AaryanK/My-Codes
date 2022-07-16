from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('dragonzpyder/',views.dragonzpyder,name='profile'),
    path('about/',views.about,name='about'),

]