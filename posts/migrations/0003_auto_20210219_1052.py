# Generated by Django 3.1.6 on 2021-02-19 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_auth_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='auth_id',
        ),
        migrations.AddField(
            model_name='post',
            name='auth_slug',
            field=models.SlugField(default=None),
        ),
    ]
