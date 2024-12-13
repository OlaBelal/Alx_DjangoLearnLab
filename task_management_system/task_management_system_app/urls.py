from django.urls import path
from .views import TaskListView
from .views import protected_view
urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),
     path('protected/', protected_view, name='protected'),
]



