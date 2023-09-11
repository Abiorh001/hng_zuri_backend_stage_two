

## ZURI BACKEND STAGE TWO APIs DOCUMENTATION

Zuri APIs is a simple RESTful API for managing user data. This README provides instructions on setting up, running, and using the APIs.


## Getting Started

### Prerequisites

Before you begin, ensure you have the following:

- Python (>=3.6)
- pip (Python package manager)

### Installation

1. Clone the GitHub repository:

   git clone https://github.com/Abiorh001/hng_zuri_backend_stage_two.git

2. Navigate to the project directory:

   cd hng_zuri_backend_stage_two


3. Install the required Python packages:

   pip install -r requirements.txt
   

4. Apply database migrations:

   python manage.py makemigrations
   python manage.py migrate


5. Start the development server:

   python manage.py runserver

   The API will be accessible at `http://localhost:8000/api`.

## Usage

The Zuri APIs provide the following endpoints for managing user data:

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