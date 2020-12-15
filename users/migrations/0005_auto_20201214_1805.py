# Generated by Django 3.1.1 on 2020-12-14 11:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0004_git_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='git',
            name='git',
            field=models.CharField(default='#', max_length=100),
        ),
        migrations.AlterField(
            model_name='phone',
            name='phone',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]