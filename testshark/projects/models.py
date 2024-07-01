# projects/models.py
from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    """Model for a testing project."""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    source_code_file = models.FileField(upload_to='source_code', blank=True, null=True)

    def __str__(self):
        return self.name
