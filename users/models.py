from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from PIL import Image
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  bio = models.TextField(max_length=200, blank=True,)
  picture = CloudinaryField('image', blank=True,)
  firstname = models.CharField(blank=True, max_length=120)
  lastname = models.CharField(blank=True, max_length=120)

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)
    SIZE = 250, 250

  def __str__(self):
    return self.user.username

  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
    if created:
      Profile.objects.create(user=instance)

  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


        