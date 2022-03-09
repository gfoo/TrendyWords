from app.models import Project
from django.db import models
from django_celery_beat.models import PeriodicTask


class Harvester(models.Model):
    name = models.TextField(unique=True)
    periodic_task = models.ForeignKey(
        PeriodicTask, null=False, on_delete=models.CASCADE)
    project = models.ForeignKey(Project,  null=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Harvester: {self.name} ({self.periodic_task})"
