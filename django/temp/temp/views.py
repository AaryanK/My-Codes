from django.shortcuts import render,HttpResponse
import datetime
'''from myapp.models import Contact
from django.contrib import messages'''

def index(request):
    return HttpResponse('<h1>hello,this is our index page</h2>')


def aaryan(request):
    return HttpResponse('<h1>hello,this is our aaryan\'s page</h2>')