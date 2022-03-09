from django.shortcuts import get_object_or_404, render
from harvester.models import Harvester

from .models import Project


def projects(request):
    projects = Project.objects.order_by('name')
    context = {'projects': projects}
    return render(request, 'projects.html', context)


def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    harvesters = project.harvester_set.all()
    return render(request, 'project/detail.html',
                  {
                      'project': project,
                      'harvesters': harvesters}
                  )
