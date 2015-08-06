import datetime
import hashlib

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.contrib.auth.models import User

from .models import Announce, City, Country, Activation
from .forms import AnnounceForm, MyRegistrationForm

def homePage(request):
	template = 'crosspay/index.html'
	recent = Announce.objects.filter(completed=False).order_by('-created')[:100]
	context = {'recent': recent}
	return render(request, template, context)

def find(request, **arg):
	template = 'crosspay/countries.html'
	context = {'current_view': 'find'}

	if len(arg) == 2 :
		template = 'crosspay/announcement_list.html'
		context['desh'] = Country.objects.get(iso_code=arg['desh'].upper())
		context['bdesh'] = Country.objects.get(iso_code=arg['bdesh'].upper())

		announcement_list = Announce.objects.filter(completed=False).filter(foreignCountry__iso_code=arg['desh'].upper()).filter(localCountry__iso_code=arg['bdesh'].upper()).order_by('-created')
		context['announcement_list'] = announcement_list

	elif len(arg) == 1:
		countries = Country.objects.all()
		context['countries'] = countries
		context['page_title'] = "And to which country?"
	else:
		countries = Country.objects.all()
		context['countries'] = countries
		context['page_title'] = "From where you want to send money?"

	return render(request, template, context)

@login_required
def announce(request, **kwargs):
	template = 'crosspay/countries.html'
	context = {'current_view': 'announce'}

	if len(kwargs) == 2 :
		template = 'crosspay/announce.html'
		context['deshName'] = Country.objects.get(iso_code=kwargs['desh'].upper())
		context['bdeshName'] = Country.objects.get(iso_code=kwargs['bdesh'].upper())

		if request.method == "POST":
			form = AnnounceForm(kwargs['desh'].upper(), kwargs['bdesh'].upper(), request.POST)
			if form.is_valid():
				announcement = form.save(commit=False)
				announcement.author = request.user
				announcement.foreignCountry = Country.objects.get(iso_code=kwargs['bdesh'].upper())
				announcement.localCountry = Country.objects.get(iso_code=kwargs['desh'].upper())
				announcement.save()
				return HttpResponseRedirect(reverse('announcement_detail', args=(announcement.id,)))
		else:
			form = AnnounceForm(kwargs['desh'].upper(), kwargs['bdesh'].upper())
		
		context['form'] = form	

	elif len(kwargs) == 1:
		countries = Country.objects.all()
		context['countries'] = countries
		context['page_title'] = "And to which country?"
	else:
		countries = Country.objects.all()
		context['countries'] = countries
		context['page_title'] = "From where you want to send money?"

	return render(request, template, context)

@login_required
def announcement_detail(request, **kwargs):
	template = 'crosspay/announcement_detail.html'
	context = {}
	announcement = Announce.objects.get(pk=kwargs['pk'])
	context['announcement'] = announcement
	return render(request, template, context)

def about(request):
	template = 'crosspay/about.html'
	context = {}
	return render(request, template, context)

def faq(request):
	pass

def contact(request):
	pass

def login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		template = 'crosspay/login.html'
		context = {}
		return render(request, template, context)

def register(request):
	template = 'crosspay/registration_form.html'
	context = {}

	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()

			activation = Activation()
			activation.user = get_object_or_404(User, username=form.cleaned_data['username'])
			activation.code = hashlib.sha512(str(str(datetime.datetime.now()) + activation.user.email)).hexdigest()
			activation.expires = datetime.datetime.now() + datetime.timedelta(days=7)
			activation.save()

			subject = "Activate your CrossPay account"
			msg = "Please go to the following link to activate your account. Activation url: http://www.crosspay.us/register/activate/" + activation.code
			sender = "no-reply@crosspay.us"
			to = [activation.user.email]

			send_mail(subject, msg, sender, to, fail_silently=False)

			return HttpResponseRedirect('/register/activate/')
	else:
		form = MyRegistrationForm()

	context['form'] = form
	return render(request, template, context)

@login_required
def dashboard(request):
	template = 'crosspay/dashboard.html'
	context = {}

	context['total_announcements'] = Announce.objects.filter(author=request.user).count()
	context['active_announcements'] = Announce.objects.filter(author=request.user).filter(completed=False)
	context['active_announcements_count'] = len(context['active_announcements'])
	context['archived_announcements'] = Announce.objects.filter(author=request.user).filter(completed=True)
	context['archived_announcements_count'] = len(context['archived_announcements'])

	return render(request, template, context)

@login_required
def announcement_archive(request, **kwargs):
	announcement = get_object_or_404(Announce, pk=kwargs['pk'])
	if request.user.id != announcement.author.id:
		raise Http404("Invalid! Some went wrong!")
	else:
		announcement.completed = True
		announcement.completedDate = datetime.datetime.now()
		announcement.save()
		return HttpResponseRedirect(reverse('announcement_detail', args=(announcement.id,)))

def activationView(request, **kwargs):
	template = 'crosspay/activation.html'
	context = {}

	if 'code' in kwargs.keys():
		activation = get_object_or_404(Activation, code=kwargs['code'])
		if activation.is_valid():
			user = User.objects.get(pk=activation.user.id)
			user.is_active = True
			user.save()
			activation.delete()

			context['title'] = "Success!"
			context['msg'] = "Your account is now active!"
		else:
			context['title'] = "Invalid"
			context['msg'] = "Something went wrong!"
	else:
		context['title'] = "Check your email"
		context['msg'] = "An activation link is sent to your email. Go to that link to activate your account!"

	return render(request, template, context)