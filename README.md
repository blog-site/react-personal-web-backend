# React personal web backend
Django

## Development
### Run the Backend Server for Development
- Default host on `http://127.0.0.1:8000/`
    ```
    $ python manage.py runserver
    ```

### Change the Database Schema
1. modify `<app-name>/models.py`
1. run `python manage.py makemigrations`
1. run `python manage.py migrate`

### Clear the Migrations
1. clear migrations table
    ```
    ./manage.py migrate --fake <app-name> zero
    ```
1. Remove `<app-name>/migrations/` folder or contents.
1. Make the migrations:
    ```
    ./manage.py makemigrations <app-name>
    ```
1. tidy up your migrations without making other database changes:
    ```
    ./manage.py migrate --fake <app-name>
    ```