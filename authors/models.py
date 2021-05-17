from django.db import models
from datetime import datetime

class Author(models.Model):
    name = models.CharField(max_length = 120)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    description = models.TextField(blank=True)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    hire_date = models.DateTimeField(default = datetime.now, blank = True)
    is_mvp = models.BooleanField(default=False)

    def __str__(self):
        return self.name