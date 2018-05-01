from django.contrib import admin
from .models import Class, Item, Assignment, Calendar, RedemptionPage


# Register your models here.
admin.site.register(Class)
admin.site.register(Item)
admin.site.register(Assignment)
admin.site.register(Calendar)