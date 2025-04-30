# Project Introduction

Representational Systems Quiz App
This project is a web application built with Django that allows users to take a quiz to determine their dominant representational system (Visual, Auditory, Kinesthetic, Olfactory, Gustatory, Auditory Digital) based on their answers. The application provides an interface for users to take the quiz and an admin panel for managing quiz content and viewing results.

## Table of Contents
  - [Features](#Features)
  - [TechnologiesUsed](#TechnologiesUsed)
  - [SetUpAndInstallation](#SetUpAndInstallation)
  - [ProjectStructure](#projectstructure)
  - [AdminInterface](#admininterface)


### Features
 - Quiz Interface: A user-friendly interface to take the quiz.
 - Category Selection: Option to filter questions by category (if implemented in the frontend).
 - Quiz Submission: Submit answers and receive a calculated result.
 - Result Display: View the dominant representational system based on quiz answers.
### Admin Panel:
  - Manage quiz categories.
  - Add, edit, and delete questions and their corresponding answers.
  - Associate answers with specific representational systems.
  - View submitted quiz results and the calculated counts for each system.
  - API Endpoints: Provides API endpoints for fetching quiz data and submitting answers, allowing for a dynamic frontend
    implementation.

### Technologies Used
 - Backend: Python, Django
 - Database: SQLite (default, can be configured for others)
 - Frontend: HTML, CSS, JavaScript (implied by template and static files)

### Setup and Installation

- Clone the repository:
   - git clone <repository_url>
   - cd <repository_directory>
- Create a virtual environment:
   - python -m venv venv
- Activate the virtual environment:
   - On Windows:venv\Scripts\activate
   - On macOS and Linux:source venv/bin/activate
- Install dependencies:
   - pip install Django django-extensions
- Apply database migrations:
   - python manage.py migrate
- Create a superuser (for accessing the admin panel):
   - python manage.py createsuperuser
   - Follow the prompts to create a username and password.
- Start the Django development server:
   - python manage.py runserver

### Project Structure
  - manage.py: Django's command-line utility.
  - home/: The main Django app directory.
     - __init__.py: Initializes the app.
     - admin.py: Configures the Django admin interface for models.
     - asgi.py: ASGI entry point for the project.
     - models.py: Defines the database models (Category, Question, Answer, QuizResult).
     - settings.py: Project settings (database, installed apps, static files, etc.).
     - urls.py: Defines URL patterns for the app.
     - views.py: Contains the view functions that handle requests and return responses.
  - templates/: Directory for HTML template files.
  - static/: Directory for static files like CSS and JavaScript.
  - db.sqlite3: The default SQLite database file (created after running migrations).

### Admin Interface 
 - Use the superuser credentials you created during setup to log in.
 - In the admin panel, you can:
   - Add and manage Categories.
   - Add and manage Questions, including adding multiple Answers for each question and assigning a Representational System to each answer.
   - View and manage submitted Quiz Results.
  
 - API Endpoints
      - GET /api/get_quiz/: Fetches quiz questions. Can optionally accept a category query parameter to filter questions by category.
      - POST /api/submit_quiz/: Submits quiz answers. Expects a JSON payload containing a list of selected answer UIDs. Returns the UID of the created QuizResult.
  
  
