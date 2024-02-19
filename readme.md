# Projekt Event Manager (GFU Django)

## 1) Virtuelles Environemt anlegen

    cd django_projects
    python -m venv .envs/eventenv

## 2) Virutelles Enviroment aktivieren und pip-tools installieren

    eventenv\Scripts\activate
    pip install pip-tools


## 3) Requirements.in Datei anlegen und kompilieren


    mkdir event_manager
    cd event_manager

    touch requirements.in
    
    pip-compile requirements.in 
    pip-sync requirements.txt