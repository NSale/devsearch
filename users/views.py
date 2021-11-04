from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import Profile


# Create your views here.
def login_page(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print('Username does not exist!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            print('Username OR password is not correct!')

    return render(request, 'users/login_register.html')


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
