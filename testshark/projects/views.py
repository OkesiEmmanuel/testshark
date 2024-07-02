from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Project
from .forms import ProjectForm

app_name = 'projects'  # Define an app name for namespace

# Function-based View for Project Creation
@login_required
def project_create_view(request):
    """View to create a new project."""
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect('dashboard')
    else:
        form = ProjectForm()
    return render(request, 'project_create.html', {'form': form})

# Function-based View for Project Details
@login_required
def project_detail(request, pk):
    """View to display details of a specific project."""
    project = get_object_or_404(Project, pk=pk)
    
    context = {
        'project': project,
        'source_code_file': project.source_code_file,
        # Add a link or button to call the 'suggest_testcase' view
        'suggest_url': reverse('test_cases:suggest_test_cases', kwargs={'pk': project.pk}),
    }
    return render(request, 'project_detail.html', context)

# Function-based View for Project List
@login_required
def project_list(request):
    """View to list all projects for the current user."""
    projects = Project.objects.filter(owner=request.user)
    return render(request, 'project_list.html', {'projects': projects})

# Function-based View for Project Update
@login_required
def project_update_view(request, pk):
    """View to update an existing project."""
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'project_update.html', {'form': form, 'project': project})

# Function-based View for Project Deletion
@login_required
def project_delete_view(request, pk):
    """View to delete a specific project."""
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('dashboard')
    return render(request, 'project_delete.html', {'project': project})

