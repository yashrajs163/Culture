from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICES = [
    ('To Do', 'To Do'),
    ('In Progress', 'In Progress'),
    ('Done', 'Done'),
]

ASSIGNMENT_CHOICES = [
    ('Assigned', 'Assigned'),
    ('Unassigned', 'Unassigned'),
]

PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, default='In Progress')

    def __str__(self):
        return self.title
    
    
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    assigned_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # replace it with a ForeignKey to your User model
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='To Do')
    assignment_status = models.CharField(max_length=20, choices=ASSIGNMENT_CHOICES, default='Unassigned')


    def __str__(self):
        return self.title