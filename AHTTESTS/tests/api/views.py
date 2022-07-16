from django.shortcuts import render
import json
from django.http.response import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .Ticketsectors import main

from rest_framework.parsers import JSONParser

# Create your views here.
@api_view(['GET'])
def domestic_search(request):
    date = request.query_params.get('date')
    dest = request.query_params.get('dest')
    MONTHS = {"01":"JAN","02":"FEB","03":"MAR","04":"APR","05":"MAY","06":"JUN","07":"JUL","08":"AUG","09":"SEP","10":"OCT","11":"NOV","12":"DEC"}
    yy = str(date[0:4])
    mm = str(date[5:7])
    dd = str(date[8:10])
    frm = str(dest[0:3])
    to =str(dest[4:])
    
    json = main.search_for_flights(dd,MONTHS[mm],yy,frm,to)
    return Response(json)