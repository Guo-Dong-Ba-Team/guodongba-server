from django.http import Http404
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.db import connection
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib import auth
import os.path
from business.forms import *
from business.models import * 

# image is necessary. first pip install image
import image
import datetime


def register(request):
	errors = []
	if request.method == "POST":
		post = request.POST
		post_keys = post.keys()
		login_type = 1
		username = ""

		if 'p_username' in post_keys:
			login_type  = 0
			username = request.POST['p_username']
			form = RegisterForm({'user_name':request.POST['p_username'], 'login_type':0, 
				'phone_num':request.POST['p_username'], 'password':request.POST['p_password']
				})
		else:
			username = request.POST['m_username']
			form = RegisterForm({'user_name':request.POST['m_username'], 'login_type':1, 
				'email':request.POST['m_username'], 'password':request.POST['m_password']
				})

		if User.objects.filter(username=username):
			errors.append('该手机号或邮箱已注册')

		else:
			today = datetime.date.today()
			if form.is_valid():
				if login_type == 0:
					new_user_p = User.objects.create_user(request.POST['p_username'], 'null@null', request.POST['p_password']);
					new_user_p.save()
					new_business_user_p = BusinessUser(user=new_user_p, user_name=request.POST['nickname'], login_type=0, register_date = today, 
					phone_num=request.POST['p_username'], email='null@null', password=request.POST['p_password']
					)
					new_business_user_p.save()
				else:
					new_user_m = User.objects.create_user(request.POST['m_username'], request.POST['m_username'], request.POST['m_password']);
					new_user_m.save()
					new_business_user_m = BusinessUser(user=new_user_m, user_name=request.POST['nickname'], login_type=1, register_date = today,
					email=request.POST['m_username'], phone_num='00000000000', password=request.POST['m_password']
					)
					new_business_user_m.save()

				return HttpResponseRedirect('/register_success/')
			else:
				return HttpResponseRedirect('/error/')
	else:
		form = RegisterForm()
	return render_to_response('registration/register.html', {'form': form, 'errors':errors}, context_instance=RequestContext(request))

def login(request):
	errors = []
	if request.method == "POST":
		form = LoginForm(request.POST)

		user_name = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=user_name, password=password)
		if user is not None and user.is_active:
			auth.login(request,user)
			return HttpResponseRedirect('/login_success/')
		else:
			errors.append('用户名或密码错误')	
	else:
		form = LoginForm()
	return render_to_response('registration/login.html', 
		{'form': form, 'errors': errors}, context_instance=RequestContext(request))


def register_success(request):
	return render_to_response('registration/register_success.html')

def login_success(request):
	return render_to_response('registration/login_success.html')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/index/')
def getpass(request):
	return render_to_response('registration/getpass.html')

def error(request):
	return render_to_response('error.html')
