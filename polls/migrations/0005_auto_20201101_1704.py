# Generated by Django 3.1 on 2020-11-01 10:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20201101_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 2, 10, 4, 6, 890717, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 1, 10, 4, 6, 890692, tzinfo=utc), verbose_name='date published'),
        ),
    ]
