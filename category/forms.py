from django import forms
from category.models import TaskCategory


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = TaskCategory
        fields = "__all__"
