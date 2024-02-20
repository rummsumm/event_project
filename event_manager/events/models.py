from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name = "Kategorie"
        verbose_name_plural = "Kategorien"

    name = models.CharField(max_length=100)  # SQL: Varchar 100, NOT NULL

    # null = True => in der DB nullable! Optional
    # blank = True => darf im Formular leer sein.
    sub_title = models.CharField(max_length=200, null=True, blank=True) #optionales Feld
    description = models.TextField(null=True, blank=True) # optionales Textfeld

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

    created_at = models.DateTimeField(auto_now_add=True)  # beim Erstellen des Objekts Zeitstempel eintragen 
    updated_at = models.DateTimeField(auto_now=True)  # beim Updaten des Objekts Zeitstempel eintragen

    name = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200, null=True, blank=True) 
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, 
                                 on_delete=models.CASCADE, 
                                 related_name="events")
    
    # mandatory! Django wird bei Migration nachfragen, was zu tun ist.
    date = models.DateTimeField()

    # darf nur 0, 5, 10, 15 sein (festgelegt via class Group)
    min_group = models.PositiveSmallIntegerField(choices=Group.choices, default=Group.UNLIMITED) 

    def __str__(self) -> str:
        return self.name


