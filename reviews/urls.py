from .views import project
from .views import *
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin



urlpatterns = [
  path('', index, name='index'),
  path('search/', searchproject, name='search'),
  path('project/<post_id>', project, name='project'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)