from django import forms

from category.models import TaskCategory
from task.models import TaskModel


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ["task_title", "category", "task_description"]
        widgets = {"task_description": forms.Textarea()}
        helper_texts = {"task_description": "1000 chars"}

    category = forms.ModelMultipleChoiceField(
        queryset=TaskCategory.objects.all(),
        to_field_name="category_name",
        required=True,
        widget=forms.CheckboxSelectMultiple(),
    )
