from django.shortcuts import render, redirect
from Tasks.models import Task


def home(request):
    tasks = Task.objects.all()
    params = { 'tasks_list': tasks  }
    return render(request, 'tasks.html', params)


def addtask(request):

    if request.method == 'POST':
        taskname = request.POST.get('taskname')
        taskdescription = request.POST.get('taskdescription')

        t = Task()
        t.name = taskname
        t.description = taskdescription
        t.save()

        return redirect('/')


def deletetask(request):

    if request.method == 'POST':
        id = request.POST.get('recordid')
        t = Task.objects.filter(id=id)
        t.delete()
    return redirect('/')