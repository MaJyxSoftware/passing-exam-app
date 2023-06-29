# Test App

Voici un application **Django** pour tester vos compétences sur Docker.

Essayer d'utiliser la fonctionnalité disponible de Docker afin de pouvoir lancer l'application en une seule commande (app, db, ...).

Et cela, de la façon la plus sécurisé possible!

## Installation

```bash
pip install -r src/requirements.txt
```

## Configuration

Des variables d'environement sont à utiliser pour configurer correctement l'application.

| Variable    | Valeur                              | Description                                                            |
| ----------- | ----------------------------------- | ---------------------------------------------------------------------- |
| DOMAIN      | string (defaut: `*`)                | Defini le domain autoriser                                             |
| SECRET_KEY  | string (requis)                     | Clef de sécurité pour signer et sécuriser les données sensibles        |
| DEBUG       | `true` ou `false` (defaut: `false`) | Passer l'application en mode debug                                     |
| STATIC_PATH | string (default: `/var/www`)        | Chemin vers les fichiers statiques compilés                            |
| DB_NAME     | string (requis)                     | Nom de la base de données Postgres                                     |
| DB_USER     | string (requis)                     | Utilisateur à utiliser pour se connecter à la base de données Postgres |
| DB_PASSWORD | string (requis)                     | Mot de passe pour se connecter à la base de données Postgres           |
| DB_HOST     | string (requis)                     | Adresse de la base de données Postgres                                 |
| DB_PORT     | string (requis)                     | Port de la base de données Postgres                                    |

## Prérequis

### Initialisation de la DB

```bash
./manage.py migrate
```

### Collecter les fichiers statiques

```bash
./manage.py collectstatic
```

## Lancement en local

```bash
./manage.py runserver 127.0.0.1:8000
```


## Developement

```bash
docker compose -f docker-compose.dev.yml up --build -d
```
