from django.urls import path
from . import views

app_name = "category"
urlpatterns = [
    path("", views.ShowAddCategoryForm, name="add_category_form"),
]
