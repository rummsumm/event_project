# Tag 4 

## Authentifizierung und Login

https://djangoheroes.friendlybytes.net/extended_technics/authentification.html

## Übersicht der Methoden für klassenbasierte Views

https://ccbv.co.uk/


## Django Extensions (zusätzliche Sub-Kommandos, zb. Model-Graph, Urls auflisten)

https://django-extensions.readthedocs.io
(in den settings registrieren)

zb. python manage.py show_urls

## Logging
https://realpython.com/python-logging/
Loggin in settings.py konfigurieren

## Statische Dateien

### Dateien an einem Ort sammeln, um sie später produktiv ausliefern zu können, zb. Azure, AWS, Nginx
python manage.py collectstatic

### Whitenoise

statische Dateien im Produktivbetrieb via WSGI ausliefern (gzip, mit Header versehen)
https://whitenoise.readthedocs.io/en/latest/