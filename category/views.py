from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from category.forms import AddCategoryForm
from category.models import TaskCategory


# Create your views here.


class ShowAddCategoryForm(CreateView):
    model = TaskCategory
    form_class = AddCategoryForm
    success_url = reverse_lazy("task:show_tasks")

    # Thanks to this StackOverflow page
    # https://stackoverflow.com/questions/32998300/django-createview-how-to-perform-action-upon-save

    # Showing Success message
    # for successful submission
    def form_valid(self, form):
        self.object = form.save()
        success_message = f"Added new category {form.cleaned_data.get('category_name')}"
        messages.success(self.request, success_message)
        return super().form_invalid(form)


########

# function based views ===================


# def AllCategories(req):
#     return render(req, "category/category.html")

# Showing all categories wasn't in the requirement
# class AllCategories(ListView):
#     model = TaskCategory

# def ShowAddCategoryForm(req):
#     if req.POST:
#         print("POSTED")
#         current_form = AddCategoryForm(req.POST)
#         if current_form.is_valid():
#             current_form.save()
#             success_message = (
#                 f"Added new category {current_form.cleaned_data.get('category_name')}"
#             )
#             messages.success(req, success_message)
#             return redirect("task:show_tasks")
#         else:
#             error_message = "Given category can't be stored"
#             messages.error(req, error_message)
#             return redirect("task:show_tasks")
#     form = AddCategoryForm()
#     return render(req, "category/addCategoryForm.html", {"form": form})
