# Create your views here.
from django.shortcuts import render,HttpResponse
import datetime
vars= {'year':datetime.datetime.now().strftime('%Y')}


def index(request):
    vars={'age':int(datetime.datetime.now().strftime('%Y'))-2005,'year':datetime.datetime.now().strftime('%Y')}
    return render(request,'index.html',vars)

def about(request):
    vars= {'age':int(datetime.datetime.now().strftime('%Y'))-2005,'year':datetime.datetime.now().strftime('%Y')}
    return render(request,'about.html',vars)
    

def services(request):
    vars = {'age':int(datetime.datetime.now().strftime('%Y'))-2005,'year':datetime.datetime.now().strftime('%Y')}
    return render(request,'services.html',vars)
    

def Air_Ticketing(request):
    return render(request,'Air_Ticketing.html')
    

def Vehicle_Hire(request):
    return render(request,'Vehicle_Hire.html')
    

def Travel_And_Tourism_Packs(request):
    return render(request,'Travel_And_Tourism_packs.html')
    

def Domestic_Packs(request):
    return render(request,'Domestic_Packs.html')
    

def International_Packs(request):
    return render(request,'International_Packs.html')
    

def Domestic(request):
    return render(request,'Domestic.html')
    

def International(request):
    return render(request,'International.html')
    

def support(request):
    return render(request,'support.html')
    

def login(request):
    return render(request,'login.html')
    

def user_dashboard(request):
    return render(request,'user_dashboard.html')
    

def reset_password(request):
    return render(request,'reset_password.html')
    

def Contact_Us(request):
    vars = {'age':int(datetime.datetime.now().strftime('%Y'))-2005,'year':datetime.datetime.now().strftime('%Y'),'year':datetime.datetime.now().strftime('%Y')}
    return render(request,'Contact_Us.html',vars)
    

