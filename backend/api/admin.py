from django.contrib import admin
from .models import Project, Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'assigned_user', 'due_date', 'priority', 'status', 'assignment_status')
    list_filter = ('project', 'assigned_user', 'priority', 'status', 'assignment_status')
    search_fields = ('title', 'description')
    date_hierarchy = 'due_date'

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date', 'end_date', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'description')
    date_hierarchy = 'start_date'