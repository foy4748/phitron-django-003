from django.shortcuts import render

from task.forms import AddTaskForm
from task.models import TaskModel

# Create your views here.


def AllTasks(req):
    tasks = TaskModel.objects.all()
    return render(req, "task/task.html", {"tasks": tasks})


def ShowAddTaskForm(req):
    if req.POST:
        print("POSTED")
        current_form = AddTaskForm(req.POST)
        if current_form.is_valid():
            current_form.save()
            success_message = (
                f"Added new task {current_form.cleaned_data.get('task_title')}"
            )
            return render(req, "task/task.html", {"success_message": success_message})
        else:
            error_message = "Given task can't be stored"
            return render(
                req,
                "error.html",
                {"error_message": error_message},
            )
    form = AddTaskForm()
    return render(req, "task/addTaskForm.html", {"form": form})
