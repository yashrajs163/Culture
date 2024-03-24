from django import forms
from .models import Project, Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'project', 'assigned_user', 'due_date', 'priority', 'assignment_status']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description','start_date', 'end_date', 'status']