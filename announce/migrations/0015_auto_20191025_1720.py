# Generated by Django 2.2.5 on 2019-10-25 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announce', '0014_announce_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announce',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]