from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def projects(request):
    msg = 'Hello, you\'re on the projects page.'
    return render(request, 'projects/projects.html', {
        'msg': msg,
    })


def project(request, pk):
    return render(request, 'projects/single-project.html')
