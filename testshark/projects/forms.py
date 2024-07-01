# projects/forms.py
from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    """Form for creating and editing projects."""
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control secondary-bg primary-text'}))
    description = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class':'form-control secondary-bg primary-text'}))
    source_code_file = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control secondary-bg primary-text'}))
    class Meta:
        model = Project
        fields = ("name", "description", "source_code_file")