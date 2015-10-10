from django.shortcuts import render_to_response

def home_page(request):
	return render_to_response('index.html')

def about(request):
	return render_to_response('about.html')

def contact(request):
	return render_to_response('contact.html')

def register(request):
	return render_to_response('register.html')

def login(request):
	return render_to_response('login.html')

def getpass(request):
	return render_to_response('getpass.html')
