from django.contrib import admin

from profiles_api import models

"""First version"""
admin.site.register(models.UserProfile)

admin.site.register(models.ProfileFeedItem)

"""Upgraded version"""

'''@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(models.ProfileFeedItem)
class ProfileFeedItemAdmin(admin.ModelAdmin):
    pass'''