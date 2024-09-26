from django.shortcuts import render

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
            return render(
                req, "category/category.html", {"success_message": success_message}
            )
        else:
            error_message = "Given category can't be stored"
            return render(
                req,
                "error.html",
                {"error_message": error_message},
            )
    form = AddCategoryForm()
    return render(req, "category/addCategoryForm.html", {"form": form})
