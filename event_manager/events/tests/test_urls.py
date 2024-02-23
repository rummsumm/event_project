from http import HTTPStatus
import logging
from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from events.models import Event, Category
from events.factories import EventFactory


def create_user():
    return get_user_model().objects.create_user(username="bob", password="abc")


class EventUrlsTest(TestCase):
    """Tests der öffentlichen Endpunkte."""

    @classmethod
    def setUpClass(cls):
        """wird einmal vor allen Tests in der Klasse ausführt"""
        super().setUpClass()
        cls.client = Client()

    def setUp(self):
        """Wird vor jedem Test ausgeführt!"""
        user = create_user()
        self.event = EventFactory(name="XXX Event", author=user)

    def test_event_overview(self):
        """Testen, ob die Event-Overview erreichbar ist.

        ist Status-Code 200?
        ist das entsprechende Template genutzt worden?
        findet sich der Text "Übersicht der Events" in der Response
        """
        url = reverse("events:events")
        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)  # 200
        self.assertTemplateUsed(response, "events/event_list.html")
        self.assertContains(response, text="Übersicht der Events")
        self.assertContains(response, text="XXX Event")

    def test_event_detail(self):
        """Teste Event Detailseite."""
        url = reverse("events:event", args=(self.event.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "events/event_detail.html")
        self.assertContains(response, text="XXX Event")
