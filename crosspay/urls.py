"""crosspay URL Configuration

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
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from crosspayapp import views

urlpatterns = [
	url(r'^$', views.homePage, name='index'),
	url(r'^find/(?P<desh>[a-z]{2})/(?P<bdesh>[a-z]{2})/$', views.find, name='bdeshfound'),
	url(r'^find/(?P<desh>[a-z]{2})/', views.find, name='findbdesh'),
	url(r'^find/', views.find, name='find'),
	url(r'^announce/(?P<desh>[a-z]{2})/(?P<bdesh>[a-z]{2})/$', views.announce, name='announcebdeshfound'),
	url(r'^announce/(?P<desh>[a-z]{2})/', views.announce, name='announcebdesh'),
	url(r'^announce/', views.announce, name='announce'),
	url(r'^announcement/detail/(?P<pk>[0-9]+)/$', views.announcement_detail, name='announcement_detail'),
	url(r'^announcement/archive/(?P<pk>[0-9]+)/$', views.announcement_archive, name='announcement_archive'),
	url(r'^about/', views.about, name='about'),
	url(r'^faq/', views.faq, name='faq'),
	url(r'^contact/', views.contact, name='contact'),
	url(r'^accounts/', include('registration.backends.default.urls')),
	url(r'^register/$', views.register, name='register'),
	url(r'^register/activate/$', views.activationView, name='activation_link'),
	url(r'^register/activate/(?P<code>[A-Za-z0-9]{128})/$', views.activationView, name='activation_confirm'),
	url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'crosspay/login.html'}, name='login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'crosspay/logout.html'}, name='logout'),
	url(r'^privacy/', views.login, name='privacy'),
	url(r'^ula/', views.login, name='ula'),
	url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^admin/', include(admin.site.urls)),
]
