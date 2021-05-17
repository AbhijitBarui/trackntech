from django.db import models
from datetime import datetime

class Interest(models.Model):
    content = models.CharField(max_length = 150)
    name = models.CharField(max_length = 150, default="")
    content_id = models.IntegerField()
    topic = models.CharField(max_length=150)
    interest_date = models.DateTimeField(default = datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name