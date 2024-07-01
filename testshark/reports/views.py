# reports/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from scripts.models import TestScript
from .models import TestResult

@login_required
def report_view(request, pk):
    """View to display test results."""
    test_script = get_object_or_404(TestScript, pk=pk)
    results = TestResult.objects.filter(test_script=test_script)

    return render(request, 'report_view.html', {'test_script': test_script, 'results': results})