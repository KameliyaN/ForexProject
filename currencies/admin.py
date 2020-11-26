from django.contrib import admin

# Register your models here.
from currencies.models import Currency, Category, Links

admin.site.register(Currency)
admin.site.register(Category)
admin.site.register(Links)
