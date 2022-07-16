from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('route_finder',views.find_routes,name='route_finder'),
    '''path('services/Air_Ticketing',views.Air_Ticketing,name='services/Air_Ticketing/Domestic'),
    path('services/Vehicle_Hire',views.Vehicle_Hire,name='services/Air_Ticketing/Domestic'),
    path('services/Air_Ticketing/Domestic',views.Domestic,name='services/Air_Ticketing'),
    path('services/Air_Ticketing/International',views.International,name='services/Air_Ticketing/International'),
    path('services/Travel_And_Tourism_Packs',views.Travel_And_Tourism_Packs,name='services/Travel_And_Tourism_Packs'),
    path('services/Travel_And_Tourism_Packs/International_Packs',views.International_Packs,name='services/Travel_And_Tourism_Packs/International_Packs'),
    path('services/Travel_And_Tourism_Packs/Domestic_Packs',views.Domestic_Packs,name='services/Travel_And_Tourism_Packs/Domestic_Packs'),
    path('support',views.support,name='support'),
    path('login',views.login,name='login'),
    path('user_dashboard',views.user_dashboard,name='user_dashboard'),
    path('login/reset_password',views.reset_password,name='login/reset_password'),
    path('login',views.login,name='login'),
    path('Contact_Us',views.Contact_Us,name='Contact_Us'),'''

]
