from django.contrib import admin
from .models import Profile

# We always have to remember to register our models so we can view them as admins
admin.site.register(Profile)
