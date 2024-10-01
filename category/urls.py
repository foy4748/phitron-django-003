from django.urls import path
from . import views

app_name = "category"
urlpatterns = [
    path("", views.ShowAddCategoryForm.as_view(), name="add_category_form"),
]
