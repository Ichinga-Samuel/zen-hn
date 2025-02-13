## Migrations

### When having issues with migrations(dependencies reference nonexistent parent node)
- Delete all migrations files in the migrations folder except the __init__.py file
- Do the same for the pycache folder

## django-allauth
- Has an app called account which is responsible for handling user authentication
- Make sure you don't have an app called account in your project

## OpenAPI

- OpenAPI is a specification for building APIs
- Create a schema file with the following command
```bash
python manage.py spectacular --file schema.yml
```

## Secret Key

- The secret key should be stored in an environment variable
- To generate a new secret key, run the following command
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

## Using Postgres in Django

- Install the following packages
```bash
pip install psycopg2-binary
pip install dj-database-url # optional
```
