# scripts/models.py
from django.db import models
from testcases.models import TestCase
from projects.models import Project

class TestScript(models.Model):
    """Model for a generated test script."""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE)
    framework = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    script_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.test_case.name} - {self.framework} script"