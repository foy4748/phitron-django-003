from django.shortcuts import render


# Create your views here.
def AllCategories(req):
    return render(req, "category/category.html")
