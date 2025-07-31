from django.contrib import admin
from app1.models import *
# Register your models here.
admin.site.register(User)
admin.site.register(profile)
admin.site.register(Dresses)
admin.site.register(booked)
admin.site.register(Cart)