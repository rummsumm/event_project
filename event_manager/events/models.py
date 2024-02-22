from functools import partial
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from .validators import datetime_in_future, bad_word_filter


User = get_user_model()


class Category(models.Model):

    class Meta:
        verbose_name = "Kategorie"
        verbose_name_plural = "Kategorien"

    name = models.CharField(max_length=100)  # SQL: Varchar 100, NOT NULL

    # null = True => in der DB nullable! Optional
    # blank = True => darf im Formular leer sein.
    sub_title = models.CharField(max_length=200, null=True, blank=True)  # optionales Feld
    description = models.TextField(null=True, blank=True)  # optionales Textfeld

    def get_absolute_url(self):
        return reverse("events:category", kwargs={"pk": self.pk})

    def __str__(self):
        # String-Repräsentation
        # wird ausgeführt, wenn das Objekt ausgedruckt wird. toString() oder ähnlich
        return self.name


class Event(models.Model):

    class Group(models.IntegerChoices):
        SMALL = 5
        MEDIUM = 10
        BIG = 15
        UNLIMITED = 0

    created_at = models.DateTimeField(
        auto_now_add=True
    )  # beim Erstellen des Objekts Zeitstempel eintragen
    updated_at = models.DateTimeField(
        auto_now=True
    )  # beim Updaten des Objekts Zeitstempel eintragen

    name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    sub_title = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        validators=[partial(bad_word_filter, ["evil", "bad", "doof"])],
    )
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="events")

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="events"
    )  # bob.events

    # mandatory! Django wird bei Migration nachfragen, was zu tun ist.
    date = models.DateTimeField(validators=[datetime_in_future])

    # darf nur 0, 5, 10, 15 sein (festgelegt via class Group)
    min_group = models.PositiveSmallIntegerField(
        choices=Group.choices, default=Group.UNLIMITED
    )

    def related_events(self):
        """Erstelle ein Queryset von ähnlichen Objekten."""
        related_events = Event.objects.filter(
            min_group=self.min_group, category=self.category
        ).exclude(pk=self.pk)

        return related_events[:10]

    def get_absolute_url(self):
        return reverse("events:event", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.name
