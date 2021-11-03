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

    topSkills = profile_selected.skill_set.exclude(description__exact="")
    otherSkills = profile_selected.skill_set.filter(description="")

    context = {
        "profile": profile_selected,
        "topSkills": topSkills,
        "otherSkills": otherSkills,
    }
    return render(request, 'users/user-profile.html', context)
