"""guodongba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from guodongba import views as main_views
from business import views as business
from admin import views as my_admin
from guodongba import settings
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main_views.home_page),
    url(r'^index/$', main_views.home_page),
    url(r'^agreement/$', main_views.agreement),
    url(r'^register/$', business.register),
    url(r'^register_success/$', business.register_success),
    url(r'^login/$', business.login),
    url(r'^logout/$', business.logout),
    url(r'^login_success/$', business.login_success),
    url(r'^error/$', business.error),
    url(r'^getpass/$', business.getpass),
    url(r'^upload/$', my_admin.upload),
    url(r'^business/admin/$', my_admin.admin_base_view,{'template_name': 'admin/index.html'}),
    url(r'^business/admin/account/$', my_admin.admin_base_view,{'template_name': 'admin/account.html'}),
    url(r'^business/admin/form/$', my_admin.form, {'template_name': 'admin/pages/form.html'}),
    url(r'^business/admin/add/(?P<type>\w+)/$', my_admin.method_splitter, {'GET':my_admin.add_gym_get, 'POST':my_admin.add_gym_post,'template_name':'admin/pages/add/gym_add.html'}),
    url(r'^business/admin/gyms/(?P<id>\d+)/$', my_admin.show_gym),

    url(r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }), 






]