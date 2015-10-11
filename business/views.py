from django.shortcuts import render
from django.shortcuts import render_to_response

def register(request):
	return render_to_response('registration/register.html')

def login(request):
	return render_to_response('registration/login.html')

