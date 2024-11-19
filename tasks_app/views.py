from django.shortcuts import render

from .models import Task

def index(request):
    tasks_list = Task.objects.order_by("-pub_time")
    context = {
        "tasks_list": tasks_list,
    }
    return render(request, "tasks_app/index.html", context)

def details(request, id):
    task = Task.objects.filter(id=id)
    context = {
        "task": task
    }
    return render(request, "tasks_app/details.html", context)
