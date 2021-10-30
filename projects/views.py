from django.shortcuts import render, redirect
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

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {
        'form': form
    }
    return render(request, 'projects/project_form.html', context)


def update_project(request, pk):
    project_obj = Project.objects.get(id=pk)
    form = ProjectForm(instance=project_obj)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project_obj)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {
        'form': form
    }
    return render(request, 'projects/project_form.html', context)


def delete_project(request, pk):
    project_obj = Project.objects.get(id=pk)

    if request.method == 'POST':
        project_obj.delete()
        return redirect('projects')

    context = {
        'object': project_obj,
    }
    return render(request, 'projects/delete_template.html', context)
