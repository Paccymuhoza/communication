# Generated by Django 2.2.5 on 2019-09-30 15:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announce', '0008_auto_20190930_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announce',
            name='receiver',
            field=models.ManyToManyField(blank=True, null=True, related_name='zones', to=settings.AUTH_USER_MODEL),
        ),
    ]
