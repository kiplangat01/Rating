from django.db import models
from django.contrib.auth.models import User
import uuid
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
import datetime as dt
from cloudinary.models import CloudinaryField



class Project(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.CharField(max_length=120, null=True, blank=False)
  url = models.URLField(max_length=255, null=True, blank=False)
  image = CloudinaryField('image')
  technologies = models.CharField(max_length=200, blank=True)
  description = models.TextField(max_length=1200, blank=False, verbose_name='Description')
  date_posted = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return str(self.id)

  @classmethod
  def search_project(cls, title):
    return cls.objects.filter(title__icontains=title)

  def save_post(self):
    self.save()

  def delete_post(self):
      self.delete()

  @classmethod
  def all_posts(cls):
      return cls.objects.all()

class Rating(models.Model):
  rating = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
  )

  design = models.IntegerField(choices=rating, default=0, blank=True)
  usability = models.IntegerField(choices=rating, blank=True)
  content = models.IntegerField(choices=rating, blank=True)
  score = models.FloatField(default=0, blank=True)
  design_average = models.FloatField(default=0, blank=True)
  usability_average = models.FloatField(default=0, blank=True)
  content_average = models.FloatField(default=0, blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='rater')
  post = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings', null=True)