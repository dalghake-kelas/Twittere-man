# Generated by Django 3.1.6 on 2021-02-21 07:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0008_profile_followings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='followings',
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('me', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='me', to=settings.AUTH_USER_MODEL)),
                ('other_guy', models.ManyToManyField(blank=True, related_name='other_guy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
