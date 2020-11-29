# Generated by Django 3.1 on 2020-11-28 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_coin', models.CharField(default='total', max_length=200)),
                ('total_coin', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_java', models.BooleanField(default=False)),
                ('is_python', models.BooleanField(default=False)),
                ('is_JavaScript', models.BooleanField(default=False)),
                ('is_Csharp', models.BooleanField(default=False)),
                ('is_C', models.BooleanField(default=False)),
                ('is_Cpp', models.BooleanField(default=False)),
                ('is_Go', models.BooleanField(default=False)),
                ('is_R', models.BooleanField(default=False)),
                ('is_Swift', models.BooleanField(default=False)),
                ('is_PHP', models.BooleanField(default=False)),
                ('is_Kotlin', models.BooleanField(default=False)),
                ('is_Ruby', models.BooleanField(default=False)),
                ('is_Dart', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
