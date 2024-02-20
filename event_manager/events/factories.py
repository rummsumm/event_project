import factory
import random
from datetime import timedelta
from django.utils import timezone
from .models import Category, Event


categories = [
    "Sports",
    "Talk",
    "Cooking",
    "Freetime",
    "Hiking",
    "Movies",
    "Travelling",
    "Science",
    "Arts",
    "Pets",
    "Music",
    "Wellness",
]


class CategoryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Category
    
    name = factory.Iterator(categories)
    sub_title = factory.Faker("sentence")
    description = factory.Faker("paragraph", nb_sentences=5)


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event
    
    name = factory.Faker("sentence", locale="de_DE")
    sub_title = factory.Faker("sentence")
    min_group = factory.LazyAttribute(lambda _: random.choice(list(Event.Group.values)))

    date = factory.Faker(
            "date_time_between",
            start_date=timezone.now() + timedelta(days=1),
            end_date=timezone.now() + timedelta(days=400),
            tzinfo=timezone.get_current_timezone()
    )

    
