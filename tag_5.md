# Tag 5 

## Django Restframework 

https://www.django-rest-framework.org/
in den settings registrieren:

    "rest_framework",
    "rest_framework.authtoken",


## Token holen
curl -X POST -d "username=admin&password=abcd1234" http://127.0.0.1:8000/token

## Event via API eintragen
curl -X POST -d "name=abcd&category=305&min_group=5&date=2024-12-12T10" -H "Authorization: Token 227de4d07191b43fe505b9f03b8d653849fc1a05" http://127.0.0.1:8000/api/events/


## Swagger UI
https://djangoheroes.spielprinzip.com/webapi/restful_api.html#swagger
