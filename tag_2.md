# Tag 2 

## Superuser anlegen 

    python manage.py createsuperuser
    python manage.py runserver 

    http://127.0.0.1:8000/admin

## Admin

    in admin.py Model registrieren

## Meta-Class

    https://docs.djangoproject.com/en/5.0/ref/models/options/


## Querysets

    https://docs.djangoproject.com/en/5.0/ref/models/querysets/
    https://docs.djangoproject.com/en/5.0/ref/models/querysets/#field-lookups


## eigenes Subkommando erstellen

    python manage.py create_events

    ## 1. in der App Verzeichnis erstellen: 
    mkdir events/management/commands

    ## 2. Subkommand-Datei erstellen
    management/commands/create_events.py

    # Tip: argparse-lib für Kommandozeilen-Programme
    https://docs.python.org/3/library/argparse.html


## FactoryBoy installieren (in requirements-dev.in)

    pip-compile requirements-dev.in
    pip-sync requirements.txt requirements-dev.txt