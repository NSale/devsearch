from django.shortcuts import render
from .models import Profile


# Create your views here.
def profiles(request):
    all_profiles = Profile.objects.all()
    context = {
        'profiles': all_profiles,
    }
    return render(request, 'users/profiles.html', context)


def profile(request, pk):
    profile_selected = Profile.objects.get(id=pk)
    context = {
       "profile": profile_selected,
    }
    return render(request, 'users/user-profile.html', context)
