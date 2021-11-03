from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile


# @receiver(post_save, sender=User)
def profile_created(sender, instance, created, **kwargs):
    print('profile_created has been called!')
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )


# @receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    print('delete_user has been called!')
    user = instance.user
    user.delete()


post_save.connect(profile_created, sender=User)
post_delete.connect(delete_user, sender=Profile)
