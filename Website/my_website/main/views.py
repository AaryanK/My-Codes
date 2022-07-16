from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def index(response):
    return HttpResponse('<h1> Aaryan </h1>')

def tab1(response):
    return HttpResponse('<h1> tab 1 </h1>')


def checkout(response):
	return (HttpResponse('<h2> checkout </h2>'))