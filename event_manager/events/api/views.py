from rest_framework import generics, authentication, permissions
from events.models import Event, Category
from .serializers import CategorySerializer, EventSerializer


class EventListCreateView(generics.ListCreateAPIView):
    """Eine View zum Auflisten und Anlegen eines Events."""

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication]

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author)


class EventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Eine View zum Anzeigen, Editieren und Löschen eines Events."""

    queryset = Event.objects.all()
    serializer_class = EventSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    """Eine View zum Auflisten und Anlegen einer Kategorie."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Eine View zum Anzeigen, Editieren und Löschen einer Kategorie."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
