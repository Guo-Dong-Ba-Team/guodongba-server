from django.db import models

class User(models.Model):
	user_name = models.CharField(max_length=100, primary_key=True)
	login_type = models.BooleanField(verbose_name="用手机登陆还是用邮箱登陆（0为手机）")
	phone_num = models.CharField(max_length=11)
	email = models.EmailField()
	password = models.CharField(max_length=50)

class GymInfo(models.Model):
	owner = models.ForeignKey(User)
	name = models.CharField(max_length=250, primary_key=True)
	type = models.IntegerField()
	address = models.CharField(max_length=300)
	image = models.CharField(max_length=100)
	open_time = models.CharField(max_length=100)
	single_price = models.FloatField()
	vip_price = models.FloatField()
	discount = models.FloatField()
	hardware_info = models.CharField(max_length=1000)
	service_info = models.CharField(max_length=1000)

	class Meta:
		db_table = "gym_info"