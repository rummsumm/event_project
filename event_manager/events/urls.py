""" 
EVENT URLs

"""
from django.urls import path
from . import views 

app_name = "events"

urlpatterns = [ 

    # http://127.0.0.1:8000/events
    path("", views.EventListView.as_view(), name="events"),

    # http://127.0.0.1:8000/events/create
    path("create", views.EventCreateView.as_view(), name="event_create"),

    # http://127.0.0.1:8000/events/3/update
    path("update/<int:pk>", views.EventUpdateView.as_view(), name="event_update"),

    # http://127.0.0.1:8000/events/3/delete
    path("delete/<int:pk>", views.EventDeleteView.as_view(), name="event_delete"),

    # http://127.0.0.1:8000/events/3
    path("<int:pk>", views.EventDetailView.as_view(), name="event"),

    path("category/create", views.category_create, name="category_create"),
    path("category/<int:pk>/update", views.category_update, name="category_update"),

    # http://127.0.0.1:8000/events/category/3
    path("category/<int:pk>", views.category, name="category"),

    # http://127.0.0.1:8000/events/categories
    path("categories", views.categories, name="categories"),

]