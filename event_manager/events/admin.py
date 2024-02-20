from django.contrib import admin
from .models import Category, Event


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "sub_title", "event_count")  # Übersicht
    list_display_links = ("id", "name") # anklickbar
    search_fields = ["id", "name", "sub_title"]  # Suchbox erstellen
    # readonly_fields = ["author"] # readonly!

    def event_count(self, cat) -> int:
        # cat ist jeweils das Kategorie-Objekt. Über die related_name Eigentschaft "events"
        # hat man Zugriff auf die Events dieses Objekts
        return cat.events.count()


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "date", "is_active")
    # # alle Felder in Übersicht
    # list_display = [field.name for field in Event._meta.get_fields()] 
    list_display_links = ("id", "name") 
    search_fields = ["id", "name", "sub_title"] 
    actions = ["make_active", "make_inactive"]

    @admin.action(description="Setze Events auf aktiv")  # Name der Aktion in Selectbox
    def make_active(self, request, queryset):
        """Setze alle ausgewählten Einträge auf aktiv."""
        # queryset => alle ausgewählten Datensätze
        queryset.update(is_active=True)
    
    @admin.action(description="Setze Events auf inaktiv")
    def make_inactive(self, request, queryset):
        """Setze alle ausgewählten Einträge auf inaktiv."""
        queryset.update(is_active=False)
    
    # Auf der Detailseite die Informationen besser gliedern
    fieldsets = (
        (
            "Standard info", 
            {"fields": ("name", "date", "category")}),
        (
            "Detail Infos",
            {"fields": ("min_group", "sub_title", "is_active")},
        ),
    )
