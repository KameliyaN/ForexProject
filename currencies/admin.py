from django.contrib import admin

# Register your models here.
from currencies.models import Currency

admin.site.register(Currency)
