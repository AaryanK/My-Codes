from django.shortcuts import render,HttpResponse
import datetime
# Create your views here.

def about(request):
    vars= {'year':datetime.datetime.now().strftime('%Y')}
    return render(request,'about.html',vars)
    