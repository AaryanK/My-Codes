from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    context = {}
    context['products'] = Product.objects.all()
    context['categories'] = Category.objects.all()
    return render(request,'index.html',context)

def dashboard(request):
    context = {}
    context['orders'] = Order.objects.all()
    return render(request,'dashboard.html',context)