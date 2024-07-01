from django.urls import path
from .views import (
    create_new_testcase,
    test_case_list,
    test_case_detail,
    test_case_update,
    test_case_delete,
    suggest_test_cases,
)

app_name = 'testcases'  # Define an app name for namespace

urlpatterns = [
    path('projects/<int:pk>/testcases/create/', create_new_testcase, name='create_test_case'),
    path('projects/<int:pk>/testcases/', test_case_list, name='test_case_list'),
    path('testcases/<int:pk>/', test_case_detail, name='test_case_detail'),
    path('testcases/<int:pk>/update/', test_case_update, name='test_case_update'),
    path('testcases/<int:pk>/delete/', test_case_delete, name='test_case_delete'),

    # Suggested Test Cases (AJAX)
    path('projects/<int:pk>/suggest_test_cases/', suggest_test_cases, name='suggest_test_cases'),
]