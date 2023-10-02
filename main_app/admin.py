from django.contrib import admin

from .models import Soda, Consumption, Store

admin.site.register(Soda)

admin.site.register(Consumption)

admin.site.register(Store)
