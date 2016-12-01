from django.contrib import admin
from regapp.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'password']#, 'website']

admin.site.register(UserProfile)
