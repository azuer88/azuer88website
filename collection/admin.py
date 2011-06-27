from django.contrib import admin

from models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'filename', 'downloads')

admin.site.register(Item, ItemAdmin)
