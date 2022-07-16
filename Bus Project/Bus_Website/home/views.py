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

def find_routes(request):
    vars= {'age':int(datetime.datetime.now().strftime('%Y'))-2005,'year':datetime.datetime.now().strftime('%Y')}
    return render(request,'about.html',vars)