
# Task Management API using Django Rest Framework and JWT Authentication

# Description

It is a the Task Manager API built using Django Rest Framework (DRF) with JWT (JSON Web Token) authentication. This API allows users to manage tasks, create, update, delete, and list tasks in a secure and efficient manner. Developed in windows environment and sqlite database is used.


## End Points

* `GET /api/api-doc/` { Swagger documentation }

* `POST /api/users/register` { for user registration }
* `POST /api/users/login/` { for user login }
* `GET /api/users/profile/`  { for getting the logged in user information }
* `POST /api/users/tasks/`  { for creating tasks }
* `GET /api/users/tasks/`  { for getting all the tasks }
* `GET /api/users/task/<title>`  { for getting a particular task }
* `PUT /api/users/task/<title>`  { for updating the entire task }
* `PATCH /api/users/task/<title>`  { for partilly updating a particular task }
* `DELETE /api/users/task/<title>`  { for deleting a particular task }


## Get the code
* Clone the repository
  
`git clone https://github.com/MVKarthikReddy/TaskManagerAPI.git`

## Install the project dependencies

First create virtualenv, then enter the following command.

`pip install -r requirements.txt`

## Run the commands to generate the database

`python manage.py makemigrations`

`python manage.py migrate`

## Generate super user

`python manage.py createsuperuser`

## Run the server

`python manage.py runserver` the application will be running on port 8000 **http://0.0.0.0:8000/**

## Run the test

`python manage.py test`

### Authentication

- **Obtain JWT Token**: To obtain a JWT token, first one has to register using the post request:

-  `POST /api/users/register/`

  Example request body:
  ```json
  {
    "username": "yourusername",
    "email": "youremail",
    "password": "yourpassword",
    "conformpassword": "yourpassword"
  }
  ```

  Example response:
   ```json
  {
    "msg": "Registration Succesful"
  }
  ```

  `POST /api/users/login/`

  Example request body:
  ```json
  {
    "username": "yourusername",
    "password": "yourpassword"
  }
  ```

  Example response:
  ```json
  {
    "access-token": "your_access_token",
    "refresh-token": "your_refresh_token",
    "msg": "Login Success"
  }
  ```

  Include the obtained token in the `Authorization` header for subsequent requests.

### Task Operations

- **List Tasks**: Retrieve a list of all tasks.

  `GET /api/users/tasks/`

- **Create Task**: Create a new task.

  `POST /api/users/tasks/`

  Example request body:
  ```json
  {
    "title": "Task Title",
    "description": "Task Description"
    "due_date": "yyyy-mm-dd",
    "completed": True or False
  }
  ```

- **Retrieve Tasks**: Retrieve details of a specific task by its ID.

  `GET /api/users/tasks/`
  `GET /api/users/task/{title}/`

- **Update Task**: Update an existing task by its ID.

  `PUT /api/tasks/{title}/`
  `PATCH /api/task/{title}/` { for partial updates }

  Example request body:
  ```json
  {
    "title": "Updated Task Title",
    "description": "Updated Task Description",
    "due_date": "yyyy-mm-dd",
    "completed": True or False
  }
  ```

- **Delete Task**: Delete a task by its ID.

  `DELETE /api/task/{title}/`

## Authentication

To authenticate your requests to the API, include the JWT token in the `Authorization` header. The header format should be:

```
Authorization: Bearer your_access_token
```

## Security

Ensure that you keep your JWT tokens secure, and never share your superuser credentials. You can also implement additional security measures as needed.

