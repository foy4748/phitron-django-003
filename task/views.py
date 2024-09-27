from django.shortcuts import get_object_or_404, redirect, render

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
            # success_message = (
            #     f"Added new task {current_form.cleaned_data.get('task_title')}"
            # )
            return redirect("task:show_tasks")
        else:
            error_message = "Given task can't be stored"
            return render(
                req,
                "error.html",
                {"error_message": error_message},
            )
    form = AddTaskForm()
    return render(req, "task/addTaskForm.html", {"form": form})


def ShowEditTaskForm(req, pk):
    task_instance = get_object_or_404(TaskModel, pk=pk)
    if req.POST:
        print("POSTED")
        current_form = AddTaskForm(req.POST, instance=task_instance)
        if current_form.is_valid():
            current_form.save()
            # success_message = (
            #     f"Updated task {current_form.cleaned_data.get('task_title')}"
            # )
            return redirect("task:show_tasks")
        else:
            error_message = "Given task can't be stored"
            return render(
                req,
                "error.html",
                {"error_message": error_message},
            )
    form = AddTaskForm(instance=task_instance)
    return render(req, "task/addTaskForm.html", {"form": form})
