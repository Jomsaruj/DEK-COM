from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Coin(models.Model):
    type_coin = models.CharField(max_length=200,default="total")
    total_coin = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.total_coin}"


class Profession(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_java = models.BooleanField(default=False)
    is_python = models.BooleanField(default=False)
    is_JavaScript = models.BooleanField(default=False)
    is_Csharp = models.BooleanField(default=False)
    is_C = models.BooleanField(default=False)
    is_Cpp = models.BooleanField(default=False)
    is_Go = models.BooleanField(default=False)
    is_R = models.BooleanField(default=False)
    is_Swift = models.BooleanField(default=False)
    is_PHP = models.BooleanField(default=False)
    is_Kotlin = models.BooleanField(default=False)
    is_Ruby = models.BooleanField(default=False)
    is_Dart = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}"


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profession.objects.create(user=instance)
    instance.profession.save()








