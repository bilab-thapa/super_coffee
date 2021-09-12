from django.urls import path
from . import views

urlpatterns = [
    path('category_form', views.category_from)
]