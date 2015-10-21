# -*- coding: utf-8 -*-
from django import forms

class RegisterForm(forms.Form):
	user_name = forms.CharField(max_length=100)
	login_type = forms.BooleanField(required=False)
	phone_num = forms.CharField(max_length=11, required=False)
	email = forms.CharField(max_length=100, required=False)
	password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
	user_name = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput)
	
class UploadFileForm(forms.Form):
	title = forms.CharField(max_length=100)
	file = forms.FileField()
	image = forms.ImageField()
	