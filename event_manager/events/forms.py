from django import forms 
from .models import Category, Event


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__" # ("name", "sub_title")


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        exclude = ("author",)

        labels = {
            "name": "Name des Events",
            "min_group": "Mindestgröße",
            "date": "Termin"
        }

        widgets = {
            "date": forms.DateInput(
                format=("%Y-%m-%d %H:%M"), attrs={"type": "datetime-local"}
            ),
            "min_group": forms.RadioSelect()
        }