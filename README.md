# CodeWise – Coding Practice Question API

CodeWise is a backend application built using Python, Django, and Django REST Framework to manage coding practice questions through RESTful APIs. It supports creating, retrieving, updating, and deleting questions, with serializer-based validation and structured JSON responses.

## Features

- Create and manage coding practice questions.
- Retrieve all questions or a specific question by ID.
- Update and delete existing questions.
- Validate incoming API data using Django REST Framework serializers.
- Organize questions using language and difficulty classifications.
- Store question details, including descriptions, sample inputs, and sample outputs.

## Tech Stack

- **Language:** Python
- **Backend Framework:** Django
- **API Framework:** Django REST Framework
- **Database:** SQLite
- **API Testing:** HTTP request collection (`APIDOC.http`)

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/jisnapm/CodeWise.git
   cd CodeWise
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the environment on Windows:

   ```bash
   venv\Scripts\activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

## API Operations

| Method | Operation |
|---|---|
| GET | Retrieve questions |
| POST | Create a question |
| GET | Retrieve a question by ID |
| PUT | Update a question |
| DELETE | Delete a question |

Refer to `APIDOC.http` for example requests and JSON payloads. Update the endpoint paths below to match your URL configuration.

## Learning Objectives

This project demonstrates Django REST Framework fundamentals, including model design, serializers, class-based API views, CRUD operations, and request validation.

## Future Improvements

- Add pagination and question filtering.
- Implement automated API tests.
- Add authentication and permissions.
- Improve API documentation and deployment configuration.
