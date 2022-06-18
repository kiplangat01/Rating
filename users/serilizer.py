from rest_framework import serializers

from reviews.models import Project
from .models import Profile
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['firstname', 'lastname', 'picture', 'bio',]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'url', 'description', 'technologies', 'image', 'posted', 'user']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'profile', 'posts']