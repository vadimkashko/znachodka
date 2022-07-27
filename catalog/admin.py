from django.contrib import admin

from catalog.models import Item, Contact, Category

admin.site.register((Item, Contact, Category))
