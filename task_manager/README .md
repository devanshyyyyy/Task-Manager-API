# Task Manager API

A simple Task Management API built with Django and Django Rest Framework (DRF) that allows users to create, read, update, and delete tasks. The API includes token-based authentication, task filtering, pagination, custom permissions, and Docker setup for local development.

## Features
- **User Authentication**: Secure token-based authentication with JWT.
- **Task CRUD Operations**: Create, read, update, and delete tasks.
- **Task Filtering**: Filter tasks by completion status and date ranges.
- **Pagination**: Display tasks in pages (default limit: 10 tasks per page).
- **Custom Permissions**: Only the user who created a task can update or delete it, while admins can view all tasks.
- **Error Handling**: User-friendly and appropriate HTTP status codes.
- **Docker**: Dockerized setup for easy local development.

## Requirements
- Python 3.x
- Django 4.x
- Django Rest Framework
- Docker (for Dockerized setup)

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/Task-Manager-API.git
   cd Task-Manager-API

2. Install dependencies:
Set up a virtual environment:
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

Install the required packages:
pip install -r requirements.txt

3. Environment variables:
Create a .env file in the project root to store environment variables (e.g., secret keys, database info).

4. Apply migrations:
python manage.py migrate

5. Run the server:
python manage.py runserver


Docker Setup (Optional)

1. Build and start the container:
docker-compose up --build

2. Access the API: Go to http://127.0.0.1:8000/api/


API Endpoints

Method	Endpoint	Description
POST	/api/token/	Obtain JWT token
GET	/api/tasks/	List all tasks
POST	/api/tasks/	Create a new task
GET	/api/tasks/{id}/	Get details of a specific task
PUT	/api/tasks/{id}/	Update a task
DELETE	/api/tasks/{id}/	Delete a task


Task Filtering

Filter tasks by completion status or date range with query parameters:

?completed=true
?created_after=YYYY-MM-DD
Testing the API

Use Postman or cURL to test API endpoints. For example, to create a task, send a POST request with task data to http://127.0.0.1:8000/api/tasks/.

