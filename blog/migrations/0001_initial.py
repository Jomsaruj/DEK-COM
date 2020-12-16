# Generated by Django 3.1 on 2020-12-16 06:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2020, 12, 16, 6, 41, 59, 114185, tzinfo=utc))),
                ('id_code', models.CharField(default='', max_length=6)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('all_votes', models.IntegerField(default=0)),
                ('poll_id_code', models.CharField(default='', max_length=6)),
                ('id_code', models.CharField(default='', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='IdCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=15)),
                ('post_num', models.BigIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('blog_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.blog')),
                ('content', models.CharField(max_length=200)),
                ('end_date', models.DateTimeField(default=datetime.datetime(2020, 12, 23, 6, 41, 59, 121180, tzinfo=utc))),
                ('choices', models.ManyToManyField(to='blog.Choice')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('blog.blog',),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('blog_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.blog')),
                ('content', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('blog.blog',),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('blog_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.blog')),
                ('content', models.CharField(max_length=200)),
                ('is_closed', models.BooleanField(default=False)),
                ('solution_id_code', models.CharField(default='', max_length=6)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('blog.blog',),
        ),
        migrations.CreateModel(
            name='SubComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 12, 16, 6, 41, 59, 128190, tzinfo=utc))),
                ('comment_id_code', models.CharField(default='', max_length=6)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 12, 16, 6, 41, 59, 128190, tzinfo=utc))),
                ('like', models.IntegerField(default=0)),
                ('id_code', models.CharField(default='', max_length=6)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.ManyToManyField(to='blog.Like'),
        ),
        migrations.AddField(
            model_name='blog',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_blog.blog_set+', to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.choice')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.poll')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('blog_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.blog')),
                ('content', models.CharField(max_length=200)),
                ('link', models.CharField(default='', max_length=200)),
                ('requirement', models.CharField(max_length=200)),
                ('candidates', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('blog.blog',),
        ),
    ]
