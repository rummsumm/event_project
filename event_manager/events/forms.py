from django import forms
from django.core.exceptions import ValidationError
from .models import Category, Event


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"  # ("name", "sub_title")


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        exclude = ("author",)

        labels = {
            "name": "Name des Events",
            "min_group": "Mindestgröße",
            "date": "Termin",
        }

        widgets = {
            "date": forms.DateInput(
                format=("%Y-%m-%d %H:%M"),
                attrs={"type": "datetime-local", "min": "2022-06-07T00:00"},
            ),
            "min_group": forms.RadioSelect(),
        }

    def clean_name(self) -> str:
        # die Methode clean() erzeugt das cleaned_date dict

        name = self.cleaned_data["name"]

        if not name.isalpha():
            raise ValidationError("der Name darf nur Buchstaben enthalten")

        return name

    def clean(self) -> dict:
        """Crossfield Validation. Mehrere Felder in clean anpassen."""
        super().clean()  # erzeugt cleaned_data Dict
        print("cleaned data:", self.cleaned_data)

        min_group = self.cleaned_data["min_group"]
        category = self.cleaned_data["category"]

        if min_group == 5 and category.name == "Freetime":
            raise ValidationError(
                "für die kategorie Freetime gibt es keine Gruppengröße von 5"
            )

        return self.cleaned_data
