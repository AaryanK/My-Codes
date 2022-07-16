from django.urls import path
from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.index,name='index'),
    path('tab/',views.tab1,name='tab 1'),
    path('checkout/',views.checkout,name='checkout'),
    ]