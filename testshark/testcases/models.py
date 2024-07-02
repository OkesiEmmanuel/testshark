# test_cases/models.py
from django.db import models
from projects.models import Project
from django.utils.translation import gettext_lazy as _

TEST_CASE_STATUS_CHOICES = (
    ('PASSED', _('Passed')),
    ('FAILED', _('Failed')),
    ('SKIPPED', _('Skipped')),
)


class TestCase(models.Model):
    """Model for a test case."""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    steps = models.TextField()
    expected_result = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=TEST_CASE_STATUS_CHOICES, default='SKIPPED')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    element_identifiers = models.JSONField(default=dict)
    programming_language = models.CharField(max_length=20, default='Python')

    def __str__(self):
        return self.name
