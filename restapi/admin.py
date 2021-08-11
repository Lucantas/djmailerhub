from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import *
from .forms import MailConfForm

admin.site.register(MailConf)
admin.site.register(Email)
admin.site.register(Host) 
admin.site.unregister(Group)