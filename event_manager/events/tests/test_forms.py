from http import HTTPStatus
from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict

from events.models import Event, Category
from events.factories import EventFactory


def create_user():
    return get_user_model().objects.create_user(username="bob", password="abc")


class EventFormsTest(TestCase):
    """Tests der Event Formulare."""

    @classmethod
    def setUpClass(cls):
        """wird einmal vor allen Tests in der Klasse ausführt"""
        super().setUpClass()
        cls.client = Client()

    def setUp(self):
        """Wird vor jedem Test ausgeführt!"""
        user = create_user()
        self.event = EventFactory(name="XXXEvent", author=user)

        self.payload = {
            "name": "XXXEvent",
            "sub_title": "test subtitle",
            "min_group": self.event.min_group,
            "category": self.event.category.pk,
            "date": self.event.date,
        }

    def test_create_new_event(self):
        """Prüfen, ob ein valides Event eingetragen werden kann.

        Erwartung GET: Status 200, Template und Text prüfen
        Erwartung POST: Status 302, 2 Objekte in der DB, Author muss getzt sein
        """
        url = reverse("events:event_create")
        self.client.force_login(self.event.author)

        # GET prüfen
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "events/event_form.html")
        self.assertContains(response, text="neue Event anlegen")

        # POST prüfen
        response = self.client.post(url, self.payload)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)  # 302
        self.assertEqual(Event.objects.count(), 2)

    def test_update_event(self):
        """Prüfen, ob Event upgedated werden kann.

        Erwartung GET: Status 200, Template und Text prüfen
         Erwartung POST: Status 302, 1 Objekte in der DB
        """
        # GET sparen wir uns
        # POST
        url = reverse("events:event_update", args=(self.event.pk,))
        payload = model_to_dict(self.event)
        payload["name"] = "YYYEvent"

        # nicht eingeloggt!
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

        # eingeloggt. User ist Author des Events
        self.client.force_login(self.event.author)
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Event.objects.count(), 1)
        event_exists = Event.objects.filter(name=payload["name"]).exists()
        self.assertTrue(event_exists)
        # self.assertEqual(Event.objects.first().name, "YYYEvent")
