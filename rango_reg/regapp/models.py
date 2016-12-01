from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    # website = models.URLField(blank=True)
    def __unicode__(self):
        return self.user.username

class GitHub(models.Model):
    userid = models.CharField(max_length=8)
    url = models.URLField()
