# Generated by Django 3.1 on 2020-11-11 04:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 11, 4, 2, 13, 741748, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 11, 4, 2, 13, 740478, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subcomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 11, 4, 2, 13, 741232, tzinfo=utc)),
        ),
    ]