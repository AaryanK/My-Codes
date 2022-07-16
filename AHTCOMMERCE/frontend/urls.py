from django.urls import path


from .views import *
urlpatterns = [
   path('',Home,name="Main_Home"),
   path('search_flights/',Search_flights,name="Search_Flights"),
    path('search_flights/<str:date>/<str:dest>/<int:number>',search_flights,name="results"),

]