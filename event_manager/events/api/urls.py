from django.urls import path
from . import views

urlpatterns = [
    # api/events
    path("", views.EventListCreateView.as_view()),
    path("<int:pk>", views.EventRetrieveUpdateDestroyView.as_view()),
    # api/events/categories
    path("categories", views.CategoryListCreateView.as_view()),
    path("category/<int:pk>", views.CategoryRetrieveUpdateDestroyView.as_view()),
]
