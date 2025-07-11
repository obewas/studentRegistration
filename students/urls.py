from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('students/', views.SnippetList.as_view(), name='student-list'),
    path('students/<int:pk>/', views.SnippetDetail.as_view(), name='student-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)