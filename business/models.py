from django.db import models

class User(models.Model):
	user_name = models.CharField(max_length=100, primary_key=True)
	login_type = models.BooleanField(verbose_name="用手机登陆还是用邮箱登陆（0为手机）")
	phone_num = models.CharField(max_length=11)
	email = models.EmailField()
	password = models.CharField(max_length=50)
