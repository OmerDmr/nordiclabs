from django.contrib import admin
from .models import Products



class productsAdmin(admin.ModelAdmin):

    list_display = ['prdId','used']
    list_display_links = ['prdId']

    class Meta:
        model = Products



admin.site.register(Products,productsAdmin)

