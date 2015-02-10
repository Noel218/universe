#-*- coding:utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from accounts.models import ExUserProfile

class ExUserProfileInline(admin.StackedInline):
    model = ExUserProfile
    can_delete = False
    verbose_name_plural = 'profile'

class UserAdmin(UserAdmin):
    inlines = (ExUserProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)