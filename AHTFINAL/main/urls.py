from .apis import *
from main import views
from django.urls import path


urlpatterns = [
    path('',views.home,name="home"),
    path('api/<str:date>/<str:dest>',views.api),
    path('search/<str:date>/<str:dest>/<int:number>',views.search,name="results"),
    path('search/',views.search_flights,name="search_flights"),
    path('login/',views.login,name="login"),
    path('manage_customer/',views.manage_customer,name="manage_customer"),
    path('manage_customer/?cq=<str:name>',views.customer_search,name="customer_search")


]