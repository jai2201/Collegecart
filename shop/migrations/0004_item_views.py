# Generated by Django 3.1.4 on 2021-04-05 19:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0003_auto_20210403_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='item_views', to=settings.AUTH_USER_MODEL),
        ),
    ]
