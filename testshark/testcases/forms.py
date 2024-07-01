# test_cases/forms.py
from django import forms
from .models import TestCase


class TestCaseForm(forms.ModelForm):
    """Form for creating and editing test cases."""
    class Meta:
        model = TestCase
        fields = ("name", "description", "steps", "expected_result", "element_identifiers", "programming_language")
        widgets = {
            'element_identifiers': forms.Textarea(attrs={'rows': 4}),
            'steps': forms.Textarea(attrs={'rows': 6}),
        }
