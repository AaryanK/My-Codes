from django.shortcuts import render,HttpResponse
import datetime
from myapp.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    '''context = {
        'variable':'this looks sent',
        'myname':'Aaryan'
    }'''
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
    # return HttpResponse('this is the about page')
def services(request):
    return render(request,'services.html')
    # return HttpResponse('this is the service page')

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        query=request.POST.get('Query')
        contact = Contact(name=name,email=email,query=query,date=datetime.datetime.today())
        contact.save()
        messages.success(request,' Your message has been sent successfully!')
    return render(request,'contact.html')
    # return HttpResponse('this is the contact page')