from django.db import models
from django.contrib.auth.models import User

class BusinessUser(models.Model):
	user = models.OneToOneField(User)
	user_name = models.CharField(max_length=50)
	login_type = models.BooleanField(verbose_name="用手机登陆还是用邮箱登陆（0为手机）")
	register_date = models.DateField()
	phone_num = models.CharField(max_length=11)
	email = models.EmailField()
	password = models.CharField(max_length=50)

	def __str__(self):
		return self.user_name

	class Meta:
		db_table = 'business_user'

class GymInfo(models.Model):
	owner = models.ForeignKey(BusinessUser)
	name = models.CharField(max_length=250)
	type = models.IntegerField()
	field_num = models.IntegerField()
	address_city= models.CharField(max_length=100)
	address_detail = models.CharField(max_length=100)
	longitude = models.FloatField()
	latitude = models.FloatField()
	main_image = models.CharField(max_length=100)
	open_time = models.CharField(max_length=50)
	single_price = models.FloatField()
	vip_price = models.FloatField()
	discount = models.FloatField()
	hardware_info = models.CharField(max_length=1000)
	service_info = models.CharField(max_length=1000)

	class Meta:
		db_table = "gym_info"

class GymImages(models.Model):
	gym = models.ForeignKey(GymInfo)
	path = models.CharField(max_length=500)

	class Meta:
		db_table="gym_detail_images"

class GymStarLevel(models.Model):
	gym = models.ForeignKey(GymInfo)
	star_level = models.IntegerField()

	class Meta:
		db_table='gym_star_level'



