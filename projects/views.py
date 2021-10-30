from django.shortcuts import render
from .models import Project
from .forms import ProjectForm


# Create your views here.
def projects(request):
    all_projects = Project.objects.all()
    context = {
        'projects': all_projects
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    tags = project_obj.tags.all()
    context = {
        'project': project_obj,
        'tags': tags
    }
    return render(request, 'projects/single-project.html', context)


def create_project(request):
    form = ProjectForm()
    context = { 'form': form }
    return render(request, 'projects/project_form.html', context)
