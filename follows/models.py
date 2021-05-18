from django.db import models
from datetime import datetime

class Follow(models.Model):
    name = models.CharField(max_length = 150, default="")
    author_id = models.IntegerField()
    user_id = models.IntegerField(blank=True)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name