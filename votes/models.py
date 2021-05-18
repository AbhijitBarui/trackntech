from django.db import models

class Vote(models.Model):
    content = models.CharField(max_length = 150)
    name = models.CharField(max_length = 150, default="")
    content_id = models.IntegerField()
    user_id = models.IntegerField(blank=True)
    has_upvoted = models.BooleanField(default=False)
    has_downvoted = models.BooleanField(default=False)

    def __str__(self):
        return self.name