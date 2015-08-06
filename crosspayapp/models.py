import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Country(models.Model):
	name = models.CharField(max_length=200)
	iso_code = models.CharField(max_length=2)
	currency_code = models.CharField(max_length=3)
	dialing_code = models.CharField(max_length=255)

	def __str__(self):
		return self.name.encode('utf8')

class City(models.Model):
	country = models.ForeignKey('Country')
	name = models.CharField(max_length=250)

	def __str__(self):
		return self.name.encode('utf8')

class Currency(models.Model):
	name = models.CharField(max_length=3)

	def __str__(self):
		return self.name.encode('utf8')

class Announce(models.Model):
	author = models.ForeignKey('auth.User')
	foreignCountry = models.ForeignKey('Country')
	foreignCity = models.ForeignKey('City')
	localCountry = models.ForeignKey('Country', related_name='+')
	localCity = models.ForeignKey('City', related_name='+')
	amount = models.DecimalField(max_digits=12, decimal_places=3)
	currency = models.ForeignKey('Currency')
	created = models.DateTimeField(auto_now_add=True)
	phone = models.CharField(max_length=15, blank=True)
	completed = models.BooleanField(default=False)
	completedDate = models.DateTimeField(blank=True, null=True)
	msg = models.TextField(max_length=160, blank=True, null=True)

	def __str__(self):
		return "#" + str(self.id)

	def get_amount(self):
		return str(self.amount)

	def get_currency(self):
		return str(self.currency)

class Activation(models.Model):
	user = models.ForeignKey(User)
	code = models.CharField(max_length=128)
	expires = models.DateTimeField()

	def __str__(self):
		return self.user.email

	def is_valid(self):
		return self.expires >= timezone.now()