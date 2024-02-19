from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)  # SQL: Varchar 100, NOT NULL

    # null = True => in der DB nullable! Optional
    # blank = True => darf im Formular leer sein.
    sub_title = models.CharField(max_length=200, null=True, blank=True) #optionales Feld
    description = models.TextField(null=True, blank=True) # optionales Textfeld (Text)
    
