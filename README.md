# Tasks

A task management app in Django.

Create, view, edit and delete tasks.

## Endpoints

- /tasks: Create new tasks and view their titles in descending order of
  publishing date

- /tasks/:id: Visit individual tasks to see their descriptions. Edit title and
  description. Delete individual tasks.

## How to start

- Clone this repository
- Run `pip install -r requirements.txt`
- Run `./manage.py runserver`
- Visit [localhost:8000/tasks](http://localhost:8000/tasks)

## Todo

### Features

- Implement Google login for user authentication.
- Allow admin users to store and manage Google OAuth keys for the app.
- Enable admin to invite new users by sending an email with a registration
  link.
- Use tailwind to style.
