from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User   # fill in custom user info then save it 
from django.contrib.auth.forms import UserCreationForm 

from .models import Announce, Country

class AnnounceForm(forms.ModelForm):
	def __init__(self, desh, bdesh, *args, **kwargs):
		super(AnnounceForm, self).__init__(*args, **kwargs)
		
		deshid = Country.objects.get(iso_code=desh).id
		bdeshid = Country.objects.get(iso_code=bdesh).id

		self.fields['foreignCity'].queryset = self.fields['foreignCity'].queryset.filter(country_id=bdeshid).order_by('name')
		self.fields['localCity'].queryset = self.fields['localCity'].queryset.filter(country_id=deshid).order_by('name')
		self.fields['currency'].queryset = self.fields['currency'].queryset.order_by('name')
		self.fields['msg'].widget.attrs['cols'] = 67
		self.fields['msg'].widget.attrs['rows'] = 3

	class Meta:
		model = Announce
		fields = ('foreignCity', 'localCity', 'amount', 'currency', 'phone', 'msg')


class MyRegistrationForm(UserCreationForm):
	email = forms.EmailField(required = True)
	first_name = forms.CharField(required = True)
	last_name = forms.CharField(required = True)

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

	def clean_email(self):
		email = self.cleaned_data.get('email')
		username = self.cleaned_data.get('username')

		if email and User.objects.filter(email=email).exclude(username=username).count():
			raise forms.ValidationError("Email address is already in use. Please supply a different email address.")
		return email

	def save(self,commit = True):   
		user = super(MyRegistrationForm, self).save(commit = False)
		user.email = self.cleaned_data['email']

		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.is_active = False


		if commit:
			user.save()
