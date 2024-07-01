from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse

from .models import TestCase
from .forms import TestCaseForm
from projects.models import Project
from gemini.api import suggest_test_cases
import ast  # For Python
import json

def detect_language(source_code_file):
    """Detects the language based on the file extension."""
    file_extension = source_code_file.name.split('.')[-1]

    if file_extension == "py":
        return "python"
    else:
        return "unknown"

def analyze_python_code(source_code):
    """Analyzes Python code."""
    tree = ast.parse(source_code)
    function_names = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    class_names = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    variable_names = [node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]
    return {"function_names": function_names, "class_names": class_names, "variable_names": variable_names}

@login_required
def suggest_test_cases_view(request, pk):
    """View to suggest test cases based on uploaded code."""
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        try:
            # Retrieve uploaded source code file
            source_code_file = project.source_code_file

            # Detect the language (only Python for now)
            language = detect_language(source_code_file)

            if language == "python":
                code_analysis_data = analyze_python_code(source_code_file.read())

                # Send the code analysis data to the Gemini API
                suggestions = suggest_test_cases(code_analysis_data)

                return JsonResponse({'success': True, 'suggestions': suggestions})
            else:
                # Handle unknown language (e.g., return an error)
                return JsonResponse({'success': False, 'error': 'Unsupported language.'})

        except Exception as e:
            # Handle general exceptions
            return JsonResponse({'success': False, 'error': str(e)})

    return render(request, 'suggest_test_cases.html', {'project': project})

@login_required
def create_new_testcase(request, pk):
    """View for creating a new test case for a specific project."""
    template_name = 'test_case_create.html'
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        form = TestCaseForm(request.POST)
        if form.is_valid():
            test_case = form.save(commit=False)
            test_case.project = project
            test_case.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = TestCaseForm()

    return render(request, template_name, {'form': form, 'project': project})

@login_required
def test_case_detail(request, pk):
    """View for displaying details of a specific test case."""
    test_case = get_object_or_404(TestCase, pk=pk)
    return render(request, 'test_case_detail.html', {'test_case': test_case})

@login_required
def test_case_list(request, pk):
    """View to list all test cases for a specific project."""
    project = get_object_or_404(Project, pk=pk)
    list_all_testcases = TestCase.objects.filter(project=project)
    return render(request, 'test_case_list.html', {'list_all_testcases': list_all_testcases})

@login_required
def test_case_update(request, pk):
    """View to update a specific test case."""
    test_case = get_object_or_404(TestCase, pk=pk)

    if request.method == 'POST':
        form = TestCaseForm(request.POST, instance=test_case)
        if form.is_valid():
            form.save()
            return redirect('test_case_detail', pk=test_case.pk)
    else:
        form = TestCaseForm(instance=test_case)

    return render(request, 'test_case_update.html', {'form': form, 'test_case': test_case})

@login_required
def test_case_delete(request, pk):
    """View to delete a specific test case."""
    test_case = get_object_or_404(TestCase, pk=pk)
    project_id = test_case.project.pk  # Get the project ID before deletion

    if request.method == 'POST':
        test_case.delete()
        return redirect('test_case_list', pk=project_id)

    return render(request, 'test_case_delete.html', {'test_case': test_case})