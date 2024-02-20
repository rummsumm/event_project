import random 
from django.core.management.base import BaseCommand, CommandParser
from events.models import Category, Event 
from events.factories import CategoryFactory, EventFactory

NUM_EVENTS = 100

class Command(BaseCommand):
    """Klasse für ein eigens Subkommando.
    
    Usage: python manage.py create_events n=100
    """

    def add_arguments(self, parser) -> None:

        # arparselib
        parser.add_argument(
            "-e",
            type=int,
            help="Number of events",
            required=True
        )
    

    def handle(self, *args, **kwargs):
        print("delete ojbects...")
        print("übergebene Argumente:", kwargs["e"])  

        # Rauslöschen aller Einträge
        for m in Event, Category:
            m.objects.all().delete()
        
        # Anlegen von 10 Kategorie-Objekten
        # create_batch gibt eine Liste aller erzeugten Objekte zurück
        categories = CategoryFactory.create_batch(10)

        for _ in range(NUM_EVENTS):
            EventFactory(category=random.choice(categories))
        
        print(f"Created {NUM_EVENTS}")