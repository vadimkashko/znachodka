from django.contrib import admin

from catalog.models import Item, Contact, Category


class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number',
                    'create_date', 'last_modified_date')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('is_active', 'name', 'category', 'type', 'city',
                    'description', 'create_date', 'last_modified_date',
                    'who_found', 'who_lost')


admin.site.register(Item, ItemAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Category)
