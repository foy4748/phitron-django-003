from django.urls import path
from . import views

app_name = "task"
urlpatterns = [
    # path("", views.AllTasks, name="show_tasks"),
    path("", views.AllTasks.as_view(), name="show_tasks"),
    # path("add_task/", views.ShowAddTaskForm, name="add_task_form"),
    path("add_task/", views.ShowAddTaskForm.as_view(), name="add_task_form"),
    # path("edit_task/<str:pk>/", views.ShowEditTaskForm, name="edit_task_form"),
    path(
        "edit_task/<str:pk>/", views.ShowEditTaskForm.as_view(), name="edit_task_form"
    ),
    # path("delete_task/<str:pk>/", views.DeleteSingleTask, name="delete_task"),
    path("delete_task/<str:pk>/", views.DeleteSingleTask.as_view(), name="delete_task"),
]
