from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from .apis import fetch_flights


# Create your views here.
# @check_maintainance

def flights(requests,date,fromsector,tosector):
	
	return HttpResponse

def home(request):
    return render(request,"home.html")

@unauthenticated_user
def login(request):
	if request.method == "POST":
		username = request.POST.get("email")
		password = request.POST.get("password")
		user = authenticate(request, username=username, password=password)
		if user is not None:
			auth_login(request,user)
			return redirect('home')
		else:
			messages.error(request,"Invalid username or password check your credentials again.")


	return render(request,"login.html")




@unauthenticated_user
def register(request):
	return render(request,"signup.html")