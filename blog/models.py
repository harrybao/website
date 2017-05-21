from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=14,primary_key=True)
    password = models.CharField(max_length=20)
    usermail = models.EmailField()

    def __unicode__(self):
        return self.username

