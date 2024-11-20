from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from .models import Task

def index(request):
    tasks_list = Task.objects.order_by("-pub_time")
    context = {
        "tasks_list": tasks_list,
    }
    return render(request, "tasks_app/index.html", context)

def details(request, id):
    task = Task.objects.get(id=id)
    context = {
        "task": task
    }
    return render(request, "tasks_app/details.html", context)

def create(request):
    task = Task(title=request.POST["title"], description=request.POST["description"], pub_time=timezone.now())
    task.save()
    return HttpResponseRedirect(reverse("tasks_app:index"))

def edit(request, id):
    task = Task.objects.get(id=id)
    task.title = request.POST["title"]
    task.description = request.POST["description"]
    task.pub_time = timezone.now()
    task.save()
    return HttpResponseRedirect(reverse("tasks_app:details", args=(task.id,)))

def delete(_, id):
    Task.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse("tasks_app:index"))

def login_form(request):
    return render(request, "tasks_app/login-form.html")

def login(request):
    user = authenticate(username=request.POST["username"], password=request.POST["password"])
    if user is not None:
        return HttpResponseRedirect(reverse("tasks_app:index"))
    else:
        return HttpResponse("login failed")
