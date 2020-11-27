from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from users.models import Coin


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        p = Profile.objects.create(user=instance)
        c = Coin.objects.create(type_coin="total")
        p.coin.add(c)
        p.save()
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()



