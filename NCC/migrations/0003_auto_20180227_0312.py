# Generated by Django 2.0.1 on 2018-02-26 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NCC', '0002_auto_20180227_0312'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='gender1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='gender2',
            field=models.IntegerField(default=0),
        ),
    ]
