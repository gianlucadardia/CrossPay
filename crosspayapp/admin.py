from django.contrib import admin

from .models import Announce, City, Country, Currency, Activation

class AnnouncementAdmin(admin.ModelAdmin):
	list_display = ['id', 'localCity', 'localCountry', 'foreignCity', 'foreignCountry', 'get_amount', 'get_currency', 'created', 'phone', 'author', 'completed']
	search_fields = ['id', 'localCity', 'localCountry', 'foreignCity', 'foreignCountry', 'get_amount', 'get_currency', 'created', 'phone', 'author', 'completed']
	list_filter = ['completed']

class CityInLine(admin.TabularInline):
	model = City
	extra = 1

class CityAdmin(admin.ModelAdmin):
	fieldsets = [
		('Overview', {'fields': ['name', 'country']}),
	]
	list_display = ('name', 'country')
	list_filter = ['country']
	search_fields = ['name']

class CountryAdmin(admin.ModelAdmin):
	fieldsets = [
		('Country Overview', {'fields': ['name', 'iso_code', 'currency_code', 'dialing_code']}),
	]
	# inlines = [CityInLine]
	list_display = ('name', 'iso_code', 'currency_code', 'dialing_code')
	search_fields = ['name']

class ActivationAdmin(admin.ModelAdmin):
	list_display = ('user', 'code', 'expires')

admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Announce, AnnouncementAdmin)
admin.site.register(Currency)
admin.site.register(Activation, ActivationAdmin)