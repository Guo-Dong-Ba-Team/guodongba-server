from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from business.forms import *
from business.models import * 

# image is necessary. first pip install image
import image

def register(request):
	if request.method == "POST":
		post = request.POST
		post_keys = post.keys()
		login_type = 1

		if 'p_username' in post_keys:
			login_type  = 0
			form = RegisterForm({'user_name':request.POST['p_username'], 'login_type':0, 
				'phone_num':request.POST['p_username'], 'password':request.POST['p_password']
				})
		else:
			form = RegisterForm({'user_name':request.POST['m_username'], 'login_type':1, 
				'email':request.POST['m_username'], 'password':request.POST['m_password']
				})

		if form.is_valid():
			if login_type == 0:

				new_user = User(user_name=request.POST['p_username'], login_type=0, 
					phone_num=request.POST['p_username'], email='null@null', password=request.POST['p_password']
					)
			else:
				new_user = User(user_name=request.POST['m_username'], login_type=1, 
					email=request.POST['m_username'], phone_num='00000000000', password=request.POST['m_password']
					)

			new_user.save()
			return HttpResponseRedirect('/register_success/')
		else:
			return HttpResponseRedirect('/error/')
	else:
		form = RegisterForm()
	return render_to_response('registration/register.html', {'form': form}, context_instance=RequestContext(request))

def login(request):
	errors = []
	if request.method == "POST":
		form = LoginForm(request.POST)

		user_name = request.POST['username']
		password = request.POST['password']
		try:
			user = User.objects.get(user_name=user_name, password=password)
		except User.DoesNotExist:
			errors.append('用户名或密码错误')	
		else:
			return HttpResponseRedirect('/login_success/')
	else:
		form = LoginForm()
	return render_to_response('registration/login.html', 
		{'form': form, 'errors': errors}, context_instance=RequestContext(request))


def register_success(request):
	return render_to_response('registration/register_success.html')

def login_success(request):
	return render_to_response('registration/login_success.html')

def error(request):
	return render_to_response('error.html')

def handle_upload_file(f):
	# this path can be any path, but subdirs must have been existed!
	with open('name.txt', 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

def handle_upload_image(f):
	# this path can be any path, but subdirs must have been existed!
	with open('name.jpg', 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)
			
def upload(request):
	if request.method == "POST":
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			handle_upload_file(request.FILES['file'])
			handle_upload_image(request.FILES['image'])
			HttpResponseRedirect('/index/')
	else:
		form = UploadFileForm()

	return render_to_response("upload.html", {'form': form}, context_instance=RequestContext(request))	




	