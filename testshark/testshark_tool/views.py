from django.shortcuts import render
from projects.models import Project
from testcases.models import TestCase

def dashboard_view(request):
    """Fetch the user and their related projects as well as test cases per each project """
    user = request.user
    projects = Project.objects.filter(owner=user)

    # Pre-fetch test cases for efficiency
    testcases_by_project = TestCase.objects.filter(project__in=projects).values(
        'project_id',
    ).annotate(
        testcase_count=models.Count('pk')
    )

    # Organize test case counts by project
    testcases_counts = {}
    for testcase_data in testcases_by_project:
        project_id = testcase_data['project_id']
        testcases_counts[project_id] = testcase_data['testcase_count']

    # Add test case count to project context
    for project in projects:
        project.testcase_count = testcases_counts.get(project.id, 0)

    context = {
        'projects': projects,
    }

    return render(request, 'dashboard.html', context)