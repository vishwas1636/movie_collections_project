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
![Screenshot 2024-10-13 112853](https://github.com/user-attachments/assets/cf5bdc60-7862-4e73-b0c7-fa6880e75dfc)
![Screenshot 2024-10-13 114103](https://github.com/user-attachments/assets/96ddd1e4-c533-497b-95fc-502ef66074b6)
![Screenshot 2024-10-13 114112](https://github.com/user-attachments/assets/60b80600-6cbe-4840-8596-3e8bfd2ba2e2)
![Screenshot 2024-10-13 114125](https://github.com/user-attachments/assets/c06099cf-4883-4a3c-a1e1-575292865b2a)
![Screenshot 2024-10-13 120344](https://github.com/user-attachments/assets/d0ec00ce-3a3e-4f83-b7ca-abc4e117c4d6)
![Screenshot 2024-10-13 125056](https://github.com/user-attachments/assets/a3c3f14f-189a-4977-a182-455dc034fca1)
![Screenshot 2024-10-13 112540](https://github.com/user-attachments/assets/ed42dcef-26a0-429b-ad67-8c31c463cfda)
![Screenshot 2024-10-13 112558](https://github.com/user-attachments/assets/d9540848-d32b-457d-bee6-cf95574bd71c)
![Screenshot 2024-10-13 112637](https://github.com/user-attachments/assets/2b33f5d0-6dbf-48e5-939e-f0cb55869762)
![Screenshot 2024-10-13 112659](https://github.com/user-attachments/assets/afdf74d3-f0ff-4fc8-b017-5f90fa7b468a)
![Screenshot 2024-10-13 112711](https://github.com/user-attachments/assets/1453387e-a36d-46eb-a6fe-6b61c7b4fa09)
![Screenshot 2024-10-13 112725](https://github.com/user-attachments/assets/b6ccf7e1-1432-4935-af83-e3baed3da861)
