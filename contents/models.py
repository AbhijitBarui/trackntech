from django.db import models
from datetime import datetime
from authors.models import Author

from taggit.managers import TaggableManager

class Content(models.Model):
    author = models.ForeignKey(Author, on_delete = models.DO_NOTHING)
    title = models.CharField(max_length = 200)
    topic = models.CharField(max_length = 200)
    content_date = models.DateTimeField(default = datetime.now, blank = True)
    is_published = models.BooleanField(default = True)
    photo_main = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    text_main = models.TextField(blank=True)
    photo_1 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    text_1 = models.TextField(blank=True)
    photo_2 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    text_2 = models.TextField(blank=True)
    photo_3 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    text_3 = models.TextField(blank=True)
    photo_4 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    text_4 = models.TextField(blank=True)
    photo_5 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    text_5 = models.TextField(blank=True)
    photo_6 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    text_6 = models.TextField(blank=True)
    photo_7 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    text_7 = models.TextField(blank=True)
    photo_8 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    text_8 = models.TextField(blank=True)
    #tags:
    slug = models.SlugField(unique=True, max_length=100)
    tags = TaggableManager()
    #upvotes and downvotes:

    def __str__(self):
        return self.title
