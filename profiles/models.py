from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    role = models.CharField(max_length=100, blank=True)
    contact = models.CharField(max_length=60, blank=True)
    # avatar = models.ImageField(
    #    upload_to="avatars/", default="avatars/defaylt.png", blank=True, null=True
    # )

    def __str__(self):
        return f"{self.user.username}'s profile"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
