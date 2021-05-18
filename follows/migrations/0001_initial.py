# Generated by Django 3.2.3 on 2021-05-18 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
                ('author_id', models.IntegerField()),
                ('user_id', models.IntegerField(blank=True)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
