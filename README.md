# React Personal Web Backend
## API
`BaseURI:<URl>/api/`
### Core
#### `[POST]login/`
```
headers: {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'X-CSRFToken': Cookies.get('csrftoken')
},
body: {
  username: <username>,
  password: <password>
}
```
#### `[POST]logout/`
 - Ensure csrf
```
headers: {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'X-CSRFToken': Cookies.get('csrftoken')
},
body: {
  'withCredentials': true
}
```
#### `[POST]register/`
 - Ensure csrf
```
headers: {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'X-CSRFToken': Cookies.get('csrftoken')
},
body: {
  username: <username>,
  password: <password>
}
```
#### `[DELETE]delete-account/`
 - Ensure csrf
```
headers: {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'X-CSRFToken': Cookies.get('csrftoken')
},
body: {
  'withCredentials': true
}
```
#### `[GET]session/`
```
headers: {
  'Accept': 'application/json',
  'Content-Type': 'application/json'
},
```
### Archive
#### `[GET]archive/view/`
##### Header: ` `
List all archives, but only properties: `slug`, `title`, `date_created`, `date_modified`, `date_published`, `published`.
 - Ensure csrf
```
[
  {
    "slug": "testslug3",
    "title": "testTitle3",
    "date_created": "2022-01-02T10:00:00Z",
    "date_modified": "2022-09-14T06:43:32.221152Z",
    "date_published": "2022-09-14T06:43:32.218690Z",
    "published": false
  },
  {
    "slug": "testslug2",
    "title": "testTitle2",
    "date_created": "2007-01-02T10:00:00Z",
    "date_modified": "2022-09-13T06:43:32.221152Z",
    "date_published": "2022-09-13T06:43:32.218690Z",
    "published": true
  },
  {
    "slug": "testslug1",
    "title": "testTitle1",
    "date_created": "2007-01-01T10:00:00Z",
    "date_modified": "2022-09-12T18:23:10.903240Z",
    "date_published": "2022-09-12T18:23:10.900625Z",
    "published": true
  }
]
```
##### Header: `published=true`
List all **published** archives, but only properties: `slug`, `title`, `date_created`, `date_modified`, `date_published`, `published`.
```
[
  {
    "slug": "testslug2",
    "title": "testTitle2",
    "date_created": "2022-01-02T10:00:00Z",
    "date_modified": "2022-09-13T06:43:32.221152Z",
    "date_published": "2022-09-13T06:43:32.218690Z",
    "published": true
  },
  {
    "slug": "testslug1",
    "title": "testTitle1",
    "date_created": "2022-01-01T10:00:00Z",
    "date_modified": "2022-09-12T18:23:10.903240Z",
    "date_published": "2022-09-12T18:23:10.900625Z",
    "published": true
  }
]
```
#### `[GET]archive/view/<slug>`
Show the archive with specified `slug`, with all properties: `slug`, `title`, `body`, `date_created`, `date_modified`, `date_published`, `published`.
- If archive not published then ensure csrf
```
{
  "slug": "testslug2",
  "title": "testTitle2",
  "body": "Test",
  "date_created": "2007-01-02T10:00:00Z",
  "date_modified": "2022-09-13T06:43:32.221152Z",
  "date_published": "2022-09-13T06:43:32.218690Z",
  "published": true
},
```
#### `[POST]archive/view/`
data includes properties: `slug`, `title`, `published`.
 - Ensure csrf
#### `[PATCH]archive/view/`
data includes properties: `slug`, `title`, `published`.
 - Ensure csrf
#### `[DELETE]archive/view/<slug>`
## Development
### Run the Backend Server for Development

- Default host on `http://127.0.0.1:8000/`
  ```
  $ python manage.py runserver
  ```
### Change the Database Schema

1. modify `<app-name>/models.py`
1. ```
   python manage.py makemigrations
   ```
1. ```
   python manage.py migrate
   ```
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
1. Tidy up your migrations without making other database changes:
   ```
   ./manage.py migrate --fake <app-name>
   ```
