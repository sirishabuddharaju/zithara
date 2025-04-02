from django.contrib import admin
from .models import Recipient

class Con(admin.ModelAdmin):
    list_display = ['gift_name','price']

admin.site.register(Recipient,Con)

