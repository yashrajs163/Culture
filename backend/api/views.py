from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse

from api.forms import TaskForm , ProjectForm
from .models import Project, Task
import datetime

# # Create your views here.
def current_time(request):
   current_date_time = datetime.datetime.now()
   return HttpResponse(f"The Current time: {current_date_time}")

# def projects(request):
#    return render(request, 'index.html')


def task_list(request):
   tasks = Task.objects.all()
   if request.method == 'POST':
      form = TaskForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('task-list')  # Redirect to the task list page after task creation
   else:
      form = TaskForm()
   return render(request, 'tasks.html', {'tasks': tasks, 'form': form})

def project_list(request):
   projects = Project.objects.all()
   if request.method == 'POST':
      form = ProjectForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('project-list')
   else:
      form = ProjectForm()
   return render (request, 'projects.html',{'projects': projects , 'form': form})


def update_task_status(request):
   if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
      task_id = request.POST.get('task_id')
      new_status = request.POST.get('new_status')
      
      try:
         task = Task.objects.get(id=task_id)
         task.status = new_status
         task.save()
         return JsonResponse({'success': True})
      except Task.DoesNotExist:
         return JsonResponse({'success': False, 'error': 'Task does not exist'}, status=404)
   else:
      return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)
    
def task_status_list(request):
      inprogress_tasks = Task.objects.filter(status='In Progress')
      done_tasks = Task.objects.filter(status='Done')
      todo_tasks = Task.objects.filter(status='To Do')

      return render(request, 'tasks.html', {'inprogress_tasks': inprogress_tasks, 'done_tasks': done_tasks, 'todo_tasks': todo_tasks})
