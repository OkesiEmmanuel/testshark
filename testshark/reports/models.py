# reports/models.py
from django.db import models
from scripts.models import TestScript
from django.utils.translation import gettext_lazy as _

TEST_RESULT_STATUS_CHOICES = (
    ('PASSED', _('Passed')),
    ('FAILED', _('Failed')),
    ('SKIPPED', _('Skipped')),
)

class TestResult(models.Model):
    """Model for test results."""
    test_script = models.ForeignKey(TestScript, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=TEST_RESULT_STATUS_CHOICES, default='SKIPPED')
    error_message = models.TextField(blank=True)
    screenshot = models.ImageField(upload_to='screenshots', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.test_script.test_case.name} - {self.status}"