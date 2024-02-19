# Projekt Event Manager (GFU Django)

## 1) Virtuelles Environemt anlegen

    cd django_projects
    python -m venv .envs/eventenv

## 2) Virutelles Enviroment aktivieren und pip-tools installieren

    eventenv\Scripts\activate
    pip install pip-tools


## 3) Projektverzeichnis erstellen, requirements.in Datei anlegen und kompilieren

    mkdir event_project
    cd event_project

    mkdir event_manager
    cd event_manager

    touch requirements.in
    
    pip-compile requirements.in  => erstellt requirements.txt
    pip-sync requirements.txt
    pip freeze => zeigt alle installierten Abhängigkeiten

## 4) Django Projekt erstellen

    cd event_manager
    django-admin startproject event_manager .

## 5) Runserver starten
den Django-Entwicklungsserver starten

    python manage.py runserver

## 6) eine neue App anlegen (events)
mit diesem Befehl lässt sich eine neue App anlegen:
 
     python manage.py startapp events

## 7) Model in models.py anlegen und Migrations durchführen

    python manage.py makemigrations events
    python manage.py migrate 

## 8) Objekte anlegen

    python manage.py shell

    from events.models import Category
    obj = Category(name="Test")
    obj.save()
    