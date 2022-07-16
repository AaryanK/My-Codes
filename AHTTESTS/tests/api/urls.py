from django.urls import path
from .views import *
urlpatterns = [
    path('domestic_search/',domestic_search,name="Domestic Search"),
    ]