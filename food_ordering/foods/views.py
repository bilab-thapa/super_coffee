from django.shortcuts import render, redirect
from .froms import CategoryForm, FoodForm

def category_from(request):
    context = {
        'form_category': CategoryForm,
        'activate_category': 'active'
    }

    return render(request, 'foods/category_form.html', context)

