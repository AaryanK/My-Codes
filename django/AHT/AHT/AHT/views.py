# I created this views.py
from django.http import HttpResponse
from django.shortcuts import render

def index(requests):
    vars = {'active':'home','name':'aaryan'}
    return render(requests,'index.html',vars)


def about(requests):
    vars = {'active':'about','name':'aaryan'}
    return render(requests,'index.html',vars)