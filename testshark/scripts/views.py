from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import path

from .models import TestScript
from testcases.models import TestCase
from gemini.api import generate_script
from projects.models import Project
from reports.models import TestResult

app_name = 'scripts'  # Define an app name for namespace

# Function-based View for Script Generation
@login_required
def generate_script_view(request, pk):
    """View to trigger script generation."""
    test_case = get_object_or_404(TestCase, pk=pk)
    project = test_case.project

    if request.method == 'POST':
        framework = request.POST.get('framework')
        language = request.POST.get('language')
        element_identifiers = request.POST.get('element_identifiers')

        try:
            script_content = generate_script(
                framework = framework,
                language = language,
                test_case = test_case,
                element_identifiers = element_identifiers
            )

            test_script = TestScript.objects.create(
                project = project,
                test_case = test_case,
                framework = framework,
                language = language,
                script_content = script_content
            )
            return JsonResponse({'success': True, 'script_id': test_script.id})

        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return render(request, 'script_view.html', {'test_case': test_case})

# Function-based View for Script Details
@login_required
def script_detail(request, pk):
    """View to display details of a generated script."""
    test_script = get_object_or_404(TestScript, pk=pk)
    return render(request, 'script_view.html', {'test_script': test_script})

