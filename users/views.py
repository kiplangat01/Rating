from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .serilizer import *
from reviews.models import Project
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UpdateUserProfileForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)           
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created you can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})



@login_required()
def profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
  
    # posts = Project.objects.filter(user=user).order_by('-date_posted')

    context = {
    # 'posts': posts,
    'profile':profile,
  }
    return render(request, 'users/profile.html', context)


def user_profile(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    posts = Project.objects.filter(user=user).order_by('-posted')
    
    params = {
        'profile': profile,
        'posts': posts,
    }
    return render(request, 'users/profile.html', params)

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = PostSerializer