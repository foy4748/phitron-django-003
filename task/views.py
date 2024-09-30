# from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView

# from django.shortcuts import get_object_or_404, redirect, render
# from django.contrib import messages
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.list import ListView

from task.forms import AddTaskForm
from task.models import TaskModel

# Create your views here.


class AllTasks(ListView):
    model = TaskModel


class ShowAddTaskForm(CreateView):
    model = TaskModel
    template_name = "task/addTaskForm.html"
    form_class = AddTaskForm
    # Doesn't work
    # success_url = reverse("task:show_tasks")
    success_url = reverse_lazy("task:show_tasks")


class ShowEditTaskForm(UpdateView):
    model = TaskModel
    template_name = "task/addTaskForm.html"
    form_class = AddTaskForm
    # Doesn't work
    # success_url = reverse("task:show_tasks")
    success_url = reverse_lazy("task:show_tasks")


class DeleteSingleTask(DeleteView):
    model = TaskModel
    success_url = reverse_lazy("task:show_tasks")


########

# function based views ===================

# def AllTasks(req):
#     tasks = TaskModel.objects.all()
#     return render(req, "task/task.html", {"tasks": tasks})

# def ShowAddTaskForm(req):
#     if req.POST:
#         print("POSTED")
#         current_form = AddTaskForm(req.POST)
#         if current_form.is_valid():
#             current_form.save()
#             success_message = (
#                 f"Added new task {current_form.cleaned_data.get('task_title')}"
#             )

#             messages.success(req, success_message)
#             return redirect("task:show_tasks")
#         else:
#             error_message = "Given task can't be stored"
#             messages.error(req, error_message)
#             return redirect("task:show_tasks")
#     form = AddTaskForm()
#     return render(req, "task/addTaskForm.html", {"form": form})


# def ShowEditTaskForm(req, pk):
#     task_instance = get_object_or_404(TaskModel, pk=pk)
#     if req.POST:
#         print("POSTED")
#         current_form = AddTaskForm(req.POST, instance=task_instance)
#         if current_form.is_valid():
#             current_form.save()
#             success_message = (
#                 f"Updated task {current_form.cleaned_data.get('task_title')}"
#             )
#             messages.success(req, success_message)
#             return redirect("task:show_tasks")
#         else:
#             error_message = "Given task can't be stored"
#             messages.error(req, error_message)
#             return redirect("task:show_tasks")
#     form = AddTaskForm(instance=task_instance)
#     return render(req, "task/addTaskForm.html", {"form": form})


# def DeleteSingleTask(_, pk):
#     task_instance = get_object_or_404(TaskModel, pk=pk)
#     task_instance.delete()
#     return redirect("task:show_tasks")
