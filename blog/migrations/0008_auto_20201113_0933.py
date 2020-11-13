# Generated by Django 3.1 on 2020-11-13 02:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20201111_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=6)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 13, 2, 33, 45, 286120, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 13, 2, 33, 45, 284305, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subcomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 13, 2, 33, 45, 285686, tzinfo=utc)),
        ),
    ]
