# Generated by Django 3.1 on 2020-11-11 04:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SubComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 11, 11, 4, 2, 10, 455625, tzinfo=utc))),
                ('comment_id_code', models.CharField(default='', max_length=6)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_topic', models.CharField(max_length=100)),
                ('post_content', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2020, 11, 11, 4, 2, 10, 453689, tzinfo=utc))),
                ('id_code', models.CharField(default='', max_length=6)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 11, 11, 4, 2, 10, 456290, tzinfo=utc))),
                ('like', models.IntegerField(default=0)),
                ('id_code', models.CharField(default='', max_length=6)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
            ],
        ),
    ]
