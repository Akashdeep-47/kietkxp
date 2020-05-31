from django.contrib import admin
from . models import signup
from . models import UserProfile

admin.site.register(signup)
admin.site.register(UserProfile)