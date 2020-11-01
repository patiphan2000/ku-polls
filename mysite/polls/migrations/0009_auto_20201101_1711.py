# Generated by Django 3.1 on 2020-11-01 10:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20201101_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 2, 10, 11, 16, 100318, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 1, 10, 11, 16, 100290, tzinfo=utc), verbose_name='date published'),
        ),
    ]
