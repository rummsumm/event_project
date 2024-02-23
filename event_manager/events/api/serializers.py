from rest_framework import serializers
from events.models import Event, Category


class CategorySerializer(serializers.ModelSerializer):
    """Serialisiere ein- und ausgehende Daten."""

    class Meta:
        model = Category
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    """Serialisiere ein- und ausgehende Daten."""

    author = serializers.StringRelatedField()
    # category = serializers.StringRelatedField()

    class Meta:
        model = Event
        fields = "__all__"
        # read_only_fields = ("id", "created_at", "updated_at")  # ???

        extra_kwargs = {"author": {"read_only": True}}
