from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *
def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('You are not authorized to view this page')
		return wrapper_func
	return decorator

def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		groups = []
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()
			for grp in group:
				groups.append(grp.name)


			if 'Admin' in groups:
				return view_func(request, *args, **kwargs)

			else:
				return redirect('404')
	return wrapper_function

def check_maintainance(view_func):
	def wrapper_function(request, *args, **kwargs):
		if Maintainance.objects.get(name="Main").Maintainance == "True":
			return redirect('503')
		else:
			return view_func(request,*args,**kwargs)
	return wrapper_function
