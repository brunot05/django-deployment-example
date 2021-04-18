from django.contrib import admin

# Register your models here.

from basic_app.models import UserProfileInfo, User

admin.site.register(UserProfileInfo)
