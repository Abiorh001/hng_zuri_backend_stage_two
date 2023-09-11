## ZURI BACKEND STAGE TWO APIs DOCUMENTATION

## Introduction

Welcome to  Zuri Backend stage two APIs documentation. This documentation provides details on how to use the APIs, including standard formats for requests and responses, sample usage, known limitations, and setup instructions.

## API Endpoints

### Create a New User

- Description: Creates a new user with the provided name.

- Endpoint: /api
- HTTP Method: POST
- Request Format:
  - Content-Type: application/json
  - Request Body:
    aplication/json
    {
      "name": "Abiola Adeshina"
    }

- Response Format:
  - HTTP Status: 201 Created
  - Response Body:
    application/json
    {
      "id": 1,
      "name": "Abiola Adeshina"
    }

Sample Usage:
shell
curl -X POST -H "Content-Type: application/json" -d '{"name": "Abiola Adeshina"}' https://example.com/api

### Retrieve User by Name

- Description: Retrieves user details by name.
- Endpoint: /api
- HTTP Method: GET
- Query Parameter:
  - name (string): The name of the user to retrieve.

- Response Format:
  - HTTP Status: 200 OK
  - Response Body:
    application/json
    {
      "id": 1,
      "name": "Abiola Adeshina"
    }

Sample Usage:
shell
curl https://example.com/api?name=Abiola%Adeshina

### Update User by Name

- Description: Update user details by name.
- Endpoint: /api
- HTTP Method: PUT
- Query Parameter:
  - name (string): The name of the user to update.
- Request Format:
  - Content-Type: application/json
  - Request Body:
    application/json
    {
      "name": "Abiorh Abiorh"
    }

- Response Format:
  - HTTP Status: 202 Accepted
  - Response Body:
    application/json
    {
      "id": 1,
      "name": "Abiorh Abiorh"
    }

Sample Usage:
shell
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Abiorh Abiorh"}' https://example.com/api?name=Abiola%20Adeshina

### Delete User by Name

- Description: Delete a user by name.
- Endpoint: /api
- HTTP Method: DELETE
- Query Parameter:
  - name (string): The name of the user to delete.
- Response Format:
  - HTTP Status: 204 No Content

Sample Usage:
shell
curl -X DELETE https://example.com/api?name=Jane%20Smith



### Retrieve User by ID

- Description: Retrieves user details by ID.
- Endpoint: /api/user_id
- HTTP Method: GET
- Response Format:
  - HTTP Status: 200 OK
  - Response Body:
    application/json
    {
      "id": 1,
      "name": "Abiola Adeshina"
    }

Sample Usage:
shell
curl https://example.com/api/1


### Update User by ID

- Description: Updates user details by ID.
- Endpoint: /api/user_id
- HTTP Method: PUT
- Request Format:
  - Content-Type: application/json
  - Request Body:

    {
      "name": "Abiola Adeshina"
    }

- Response Format:
  - HTTP Status: 202 Accepted
  - Response Body:
    application/json
    {
      "id": 1,
      "name": "Jane Smith"
    }

Sample Usage:
shell
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Abiorh Abiorh"}' https://example.com/api/1


### Delete User by ID

- Description: Deletes a user by ID.
- Endpoint: /api/user_id
- HTTP Method: DELETE
- Response Format:
  - HTTP Status: 204 No Content
Sample Usage:
shell
curl -X DELETE https://example.com/api/1

## Known Limitations

- The API expects name values to be strings only. Other data types are not allowed.
- The API does not handle authentication or authorization. It is open to anyone with the endpoint URLs.
- Error handling is basic and may be improved in future versions.

## Setup Instructions

To set up and run the API locally, follow these steps:

1. Clone the GitHub repository: `git clone `
2. Install the required dependencies: `pip install -r requirements.txt`
3. Create and apply database migrations: `python manage.py makemigrations` and `python manage.py migrate`
4. Run the development server: `python manage.py runserver`
5. The API will be accessible at `http://localhost:8000/api`


NOTE: You can deploy the API on a server by following your hosting provider's deployment instructions.
