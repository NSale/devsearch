from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile


# Create your views here.
def login_user(request):
    
    if request.user.is_authenticated:
        return redirect('profiles')
    
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username OR password are not valid!')

    return render(request, 'users/login_register.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'User has successfully logged out!')
    return redirect('profiles')


def profiles(request):
    all_profiles = Profile.objects.all()
    context = {
        'profiles': all_profiles,
    }
    return render(request, 'users/profiles.html', context)


def profile(request, pk):
    profile_selected = Profile.objects.get(id=pk)

    top_skills = profile_selected.skill_set.exclude(description__exact="")
    other_skills = profile_selected.skill_set.filter(description="")

    context = {
        "profile": profile_selected,
        "topSkills": top_skills,
        "otherSkills": other_skills,
    }
    return render(request, 'users/user-profile.html', context)
