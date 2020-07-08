# Reasonable Productivity Back-end

This is an api for the Reasonable Productivity system built with the Django REST Framework.

## Running Locally

1. Clone this repo
1. cd into this repo
1. Create a python virtual environment: `python -m venv venv`
1. Activate virutal environment: `source venv/bin/activate`
1. `pip install -r requirements.txt`
1. `python manage.py runserver`

## Schema

**Task**

* user_id: ForeinKey
* title: required
* description: default=''
* completed: boolean
* due_date: nullable
* created_at
* updated_at

**List**

* user_id
* name
* created_at
* updated_at

**ListItem**

* list_id
* text
* created_at
* updated_at

**User**

* email (unique, used for login)
* password

**UserProfile**

* user_id
* first_name
* last_name
* image
* fb_profile
* twitter_profile
* linkedin_profile
* website

**Project**

* user_id
* title
* description
* created_at
* updated_at
* due_date (for version 2)

## API

**/users**

* GET
* POST

**/users/:id**

* GET
* PATCH
* DELETE

**/users/:id/tasks**

* GET
* POST

**/users/:id/tasks/:task_id**

* GET
* PATCH
* DELETE

**/users/:id/lists**

* GET
* POST

**/users/:id/lists/:list_id**

* GET
* PATCH
* DELETE

**/users/:id/lists/:list_id/list-items**

* POST

**/users/:id/list-items/:item_id**

* PATCH
* DELETE

**/tasks**

* GET

**/tasks/:id**

* GET

## Roadmap

### Version 1.0

* Auth endpoints
  * Login
  * Update password, forgot password
* Add searching, sorting, filtering for tasks and lists

### Version 1.1

* Recurring Tasks
  * recurring: Boolean, default=False
  * recurring_time: nullable
  * recurring_frequency: daily, weekly, monthly, yearly
  * recurring_custom: (based off of recurring frequency option, user can choose specific days/weeks, etc.)
* Reminders

### Version 1.2

* Nested & Dependant Tasks
  * Back-end: tasks should be able to be marked as dependant and sub-tasks
  * Front-end: Users can drag tasks to be nested under other tasks, they can also

### Version 1.3

* Calendar View

### Version 1.4

* Contact integration for tasks: Users can sync with contacts

### Version 1.5

* Markdown enabled in task descriptions

### Version 1.6

* Calendar Integrations
