# Generated by Django 3.1.1 on 2020-12-14 10:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20201214_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 14, 10, 36, 2, 17623, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 14, 10, 36, 2, 24719, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='poll',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 21, 10, 36, 2, 20881, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subcomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 14, 10, 36, 2, 24306, tzinfo=utc)),
        ),
    ]
