# Generated by Django 3.2.3 on 2021-05-17 08:40

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('contents', '0004_auto_20210517_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='slug',
            field=models.SlugField(default='', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='content',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
