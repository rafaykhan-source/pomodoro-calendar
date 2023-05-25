from django.shortcuts import render
from .models import Task

def index(request):
    task_list = Task.objects.order_by("-id")[:5]
    context = {"task_list": task_list}
    return render(request, "pomodorocalendar/index.html", context)
