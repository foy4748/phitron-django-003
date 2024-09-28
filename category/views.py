from django.contrib import messages
from django.shortcuts import redirect, render

from category.forms import AddCategoryForm


# Create your views here.
def AllCategories(req):
    return render(req, "category/category.html")


def ShowAddCategoryForm(req):
    if req.POST:
        print("POSTED")
        current_form = AddCategoryForm(req.POST)
        if current_form.is_valid():
            current_form.save()
            success_message = (
                f"Added new category {current_form.cleaned_data.get('category_name')}"
            )
            messages.success(req, success_message)
            return redirect("task:show_tasks")
        else:
            error_message = "Given category can't be stored"
            messages.error(req, error_message)
            return redirect("task:show_tasks")
    form = AddCategoryForm()
    return render(req, "category/addCategoryForm.html", {"form": form})
