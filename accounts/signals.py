from django.db.models.signals import post_save
from django.contrib.auth.models import User

from accounts.models import Profile


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email,
            username=instance.username,
        )
        print("Profile Created!")


def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    print("Profile saved!")


post_save.connect(create_profile, sender=User, weak=False)
post_save.connect(save_profile, sender=User)

# def update_profile(sender, instance, created, **kwargs):
#     if not created:
#         instance.profile.first_name = instance.first_name
#         instance.profile.last_name = instance.last_name
#         instance.profile.email = instance.email
#         instance.profile.username = instance.username
#         instance.profile.save()
#         print("Profile updated!")
# post_save.connect(update_profile, sender=User, weak=False)
