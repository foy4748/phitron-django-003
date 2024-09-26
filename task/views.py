from django.shortcuts import render

# Create your views here.


def AllTasks(req):
    return render(req, "task/task.html")
