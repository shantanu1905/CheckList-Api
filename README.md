# CheckList Api
### created with django rest framework and JWT(Json Web Tokens for Authentication)

# Description
This API is created with help of Django rest framework and for user authentication , I have used JWT(Json Web Tokens). <br>
  Working of API   : In this Api user can Checklist just like todolist, but not similar to todoList . In TodoList we can only add todo ,but can't add subitems in todo . 
But in CheckList API we can create CheckList and add Subitems in created checklist .

# Api Features 
* User Authentication by JWT
* User Authorization(logedin user can only see his/her data.)
* User Can peforn CURD operation on database in order to retrive his/her data .
## Auth system

All the requests made to the API need an **Authorization header** with a valid token and the prefix **Bearer**

```Authorization: Bearer <token>```

In order to obtain a valid token it's necesary to send a request `POST /api/login/` with **username** and **password**. To register a new user it's necesary to make a request `POST /api/register` with the params/form data:
```
username String
password String
password2 String
```

## End Points
### Auth
* `POST /api/login/`
* `POST /api/register/`
* `POST /api/logout/`
* 

### Endpoints to access CheckList 
* `GET /api/checklist/`                    -- Get all CheckList data
* `POST /api/checklist/`                   -- Create CheckList data
* `GET /api/checklist/{CheckList_id}`      -- Get specific CheckList data
* `PUT /api/checklist/{CheckList_id}`      -- To Update specific CheckList data
* `DELETE /api/checklist/{CheckList_id}`   -- To Delete specific CheckList data


### Endpoints to access CheckList 
* `GET /api/checklist/`                               -- Get all CheckList data
* `POST /api/checklistItem/create/`                   -- Create CheckListItem data
* `GET /api/checklistItem/{CheckListItem_id}`         -- Get specific CheckListItem data
* `PUT /api/checklistItem/{CheckListItem_id}`         -- To Update specific CheckListItem data
* `DELETE /api/checklistItem/{CheckListItem_id}`      -- To Delete specific CheckListItem data

## Documentation
Refer this Documentation Pdf for more details **link** builded with **Django REST Swagger**

# Installation process 

## Install the system dependencies
* **git** 
* **pip**

## Get the code
* Clone the repository
`git clone https://github.com/shantanu1905/CheckList-Api.git`

## Install the project dependencies

`pip install -r requirements.txt`

## Run the command to generate the database
`python manage.py migrate`

## Generate super user
`python manage.py createsuperuser`

## Run the server
`python manage.py runserver` the application will be running on port 8000 **http://0.0.0.0:8000/**

## Enjoy API
