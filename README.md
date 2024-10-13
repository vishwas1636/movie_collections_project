# Movie Collection App

## Introduction
Welcome to the Movie Collection App! This Django-based web application allows users to create and manage collections of their favorite movies. It integrates seamlessly with a third-party movie listing API to fetch and display movies, featuring functionalities like user registration, authentication, and collection management. Additionally, the application includes a custom middleware to count and reset the number of requests made to the server, ensuring scalability and monitoring capabilities.

## Features
- **User Registration**: Users can sign up with a username and password.
- **JWT Authentication**: Securely access all endpoints except registration.
- **Movie Listing**: Display a list of movies fetched from an external API.
- **Collections Management**: Create, view, update, and delete movie collections.
- **Favorite Genres**: Display the top 3 favorite genres based on the user's collections.
- **Request Counter**: Monitor and reset the number of requests to the server.

## Setup and Installation

### 1. Clone the Repository
Open your terminal in VS Code and run:
```bash
git clone <your-repo-url>
cd <repo-directory>
```
## 2. Create a Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```
## 3. Install Dependencies
```bash
pip install -r requirements.txt
```
## 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
## 5. Run the Server
```bash
python manage.py runserver
```
## 6. Set Environment Variables
Create a `.env` file in your project root directory and set the following environment variables:

```ini
MOVIE_API_USERNAME=iNd3jDMYRKsN1pjQPMRz2nrq7N99q4Tsp9EY9cM0
MOVIE_API_PASSWORD=Ne5DoTQt7p8qrgkPdtenTK8zd6MorcCR5vXZIJNfJwvfafZfcOs4reyasVYddTyXCz9hcL5FGGIVxw3q02ibnBLhblivqQTp4BIC93LZHj4OppuHQUzwugcYu7TIC5H1
```
## 7. Run the Tests
Ensure everything is working correctly by running:

```bash
python manage.py test
```
## Project Structure
Here's an overview of the project's structure:
```
movie_project/
│
├── movie_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── services.py
│
├── movie_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── .env
```
