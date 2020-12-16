# Generated by Django 3.1.1 on 2020-12-14 11:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20201214_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 14, 11, 9, 41, 714777, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 14, 11, 9, 41, 732833, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='poll',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 21, 11, 9, 41, 724582, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subcomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 14, 11, 9, 41, 732170, tzinfo=utc)),
        ),
    ]
