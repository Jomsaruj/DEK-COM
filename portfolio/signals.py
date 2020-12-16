from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from users.models import Coin


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Create the profile of user."""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """Save the profile of the user."""
    instance.profile.save()
