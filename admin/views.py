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

PROJECT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'guodongba')

def method_splitter(request, *args, **kwargs):
	get_view = kwargs.pop('GET', None)
	post_view = kwargs.pop('POST', None)
	if request.method == 'GET' and get_view is not None:
		return get_view(request, *args, **kwargs)
	elif request.method == 'POST' and post_view is not None:
		return post_view(request, *args, **kwargs)
	raise Http404


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


## Admin part
def admin_base_view(request, template_name):
	if request.user.is_anonymous():
		return HttpResponseRedirect('/login/')
	if request.method == "GET":
		user = request.user
		business_user = BusinessUser.objects.get(user=user)
		gym_id_set=business_user.gyminfo_set.values_list('id',flat=True)
		gym_name_set = business_user.gyminfo_set.values_list('name',flat=True)
		gym_main_image_set = business_user.gyminfo_set.values_list('main_image',flat=True)
		nickname = getattr(business_user, 'user_name')
		register_date = getattr(business_user, 'register_date')
		phone = getattr(business_user, 'phone_num')
		email = getattr(business_user, 'email')
		gym_set = zip(gym_id_set, gym_name_set,gym_main_image_set)

	return render_to_response(template_name,
		{'nickname':nickname, 'register_date':register_date, 'phone':phone,'email':email,'id_set':gym_id_set,'gym_set':gym_set},
		 context_instance=RequestContext(request))

def form(request, template_name):
	if request.user.is_anonymous():
		return HttpResponseRedirect('/login/')
	if request.method == "GET":
		user = request.user
		business_user = BusinessUser.objects.get(user=user)
		gym_id_set=business_user.gyminfo_set.values_list('id',flat=True)
		gym_name_set = business_user.gyminfo_set.values_list('name',flat=True)
		gym_main_image_set = business_user.gyminfo_set.values_list('main_image',flat=True)
		nickname = getattr(business_user, 'user_name')
		register_date = getattr(business_user, 'register_date')
		phone = getattr(business_user, 'phone_num')
		email = getattr(business_user, 'email')
		gym_set = zip(gym_id_set, gym_name_set,gym_main_image_set)

		cursor = connection.cursor()
		all_order_list = []
		today_order_list = []
		unused_order_list = []
		all_order_num = 0
		today_order_num = 0
		unused_order_num = 0
		now = datetime.datetime.now()
		today = "%s-%s-%s" % (now.year, now.month, now.day)
		for gym_name in gym_name_set:
			num = cursor.execute('SELECT id, user, gym_name, order_time, reserve_time, reserve_field, status FROM order_info WHERE gym_name=%s ',[gym_name])
			all_order_num += num
			all_order_list.append(cursor.fetchall())


			num=cursor.execute('SELECT id, user, gym_name, order_time, reserve_time, reserve_field, status FROM order_info WHERE gym_name=%s AND order_time=%s',[gym_name, now])
			today_order_num += num
			today_order_list.append(cursor.fetchall())

			num=cursor.execute('SELECT id, user, gym_name, order_time, reserve_time, reserve_field, status FROM order_info WHERE gym_name=%s AND status=1',[gym_name])
			unused_order_num += num
			unused_order_list.append(cursor.fetchall())

		
	return render_to_response(template_name,
		{'nickname':nickname, 'register_date':register_date, 'phone':phone,'email':email,
		'id_set':gym_id_set,'gym_set':gym_set, 'all_order_list':all_order_list,
		'all_order_num':all_order_num, 'today_order_num':today_order_num, 'unused_order_num':unused_order_num
		},
		 context_instance=RequestContext(request))

def add_gym_get(request, template_name, type):
	if request.user.is_anonymous():
		return HttpResponseRedirect('/login/')
	if request.method == "GET":
		user = request.user
		business_user = BusinessUser.objects.get(user=user)
		gym_id_set=business_user.gyminfo_set.values_list('id',flat=True)
		gym_name_set = business_user.gyminfo_set.values_list('name',flat=True)
		gym_main_image_set = business_user.gyminfo_set.values_list('main_image',flat=True)
		nickname = getattr(business_user, 'user_name')
		register_date = getattr(business_user, 'register_date')
		phone = getattr(business_user, 'phone_num')
		email = getattr(business_user, 'email')
		gym_set = zip(gym_id_set, gym_name_set,gym_main_image_set)

		gym_dict = {'badmintion':'羽毛球馆', 'basketball':'篮球馆', 'swimming':'游泳馆', 'tableball':'台球馆', 'pingpang':'乒乓球馆','tennis':'网球馆', 'gym':'健身馆'}

	return render_to_response(template_name,
		{'nickname':nickname, 'register_date':register_date, 'phone':phone,'email':email,'id_set':gym_id_set,
			'name_set':gym_name_set, 'image_set':gym_main_image_set,'gym_set':gym_set,'type':gym_dict[type]
		},
		 context_instance=RequestContext(request))

def add_gym_post(request, template_name, type):
	if request.user.is_anonymous():
		return HttpResponseRedirect('/login/')

	gym_name = request.POST['gym_name']
	gym_single_price = request.POST['gym_single_price']
	gym_open_time = request.POST['gym_open_time']
	gym_field_num = request.POST['gym_field_num']
	gym_img = request.FILES['gym_img']
	gym_prov = request.POST['gym_prov']
	gym_city = request.POST['gym_city']
	gym_dist = request.POST['gym_dist']
	gym_service = request.POST['gym_service']
	gym_hardware = request.POST['gym_hardware']
	gym_remark = request.POST['gym_remark']

	gym_dict = {'badmintion':1, 'basketball':7, 'swimming':6, 'tableball':5, 'pingpang':2,'tennis':3, 'gym':4}
	user = request.user
	business_user = BusinessUser.objects.get(user=user)
	#upload image
	new_gym = GymInfo(owner=business_user, name=gym_name, type=gym_dict[type], field_num=gym_field_num, address_city=gym_prov+gym_city,address_detail=gym_dist,
		longitude=0,latitude=0, main_image=gym_img.name, open_time=gym_open_time, single_price=gym_single_price, vip_price=0,discount=0,
		hardware_info=gym_hardware,service_info=gym_service)
	new_gym.save()

	new_gym_detail_image=GymImages(gym=new_gym, path=gym_img.name)
	new_gym_detail_image.save()
	id = new_gym.id
	img_path = os.path.join(os.path.join(os.path.join(PROJECT_DIR, 'images'), str(id)), gym_img.name).replace('\\','/')
	os.makedirs(os.path.dirname(img_path), exist_ok=True)
	with open(img_path, 'wb+') as dst:
		for chunk in gym_img.chunks():
			dst.write(chunk)

	return HttpResponseRedirect('/business/admin/gyms/'+str(id)+'/')


def show_gym(request, id):
	if request.user.is_anonymous():
		return HttpResponseRedirect('/login/')

	business_user = BusinessUser.objects.get(user=request.user)
	if int(id) in business_user.gyminfo_set.values_list('id',flat=True):
		user = request.user
		business_user = BusinessUser.objects.get(user=user)
		id_set=business_user.gyminfo_set.values_list('id',flat=True)
		nickname = getattr(business_user, 'user_name')
		register_date = getattr(business_user, 'register_date')
		phone = getattr(business_user, 'phone_num')
		email = getattr(business_user, 'email')

		gym = GymInfo.objects.get(id=int(id))
		gym_name = gym.name
		field_num = gym.field_num

		id_list = []
		for  i in range (0, len(id_set)):
			id_list.append(id_set[i])

		cursor = connection.cursor()
		order_num=cursor.execute('SELECT id FROM order_info WHERE gym_name=%s AND status=1',[gym_name])

		return render_to_response('admin/pages/gyms/gym_base.html',
			{'nickname':nickname, 'register_date':register_date, 'phone':phone,'email':email,
			'id_set':id_set,'id':id_list.index(int(id))+1, 'gym_name':gym_name,'field_num':field_num, 'order_num':order_num},
			context_instance=RequestContext(request))
#		return render_to_response('admin/pages/gyms/'+str(id)+'.html')
	raise Http404
