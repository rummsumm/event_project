""" 
EVENT URLs

"""
from django.urls import path
from . import views 

app_name = "events"

urlpatterns = [

    # http://127.0.0.1:8000/events/category/3
    path("category/<int:pk>", views.category, name="category"),

    # http://127.0.0.1:8000/events/categories
    path("categories", views.categories, name="categories"),

]