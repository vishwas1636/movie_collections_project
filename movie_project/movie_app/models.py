import uuid
from django.db import models
from django.contrib.auth.models import User

def generate_uuid():
    return str(uuid.uuid4())

class Collections(models.Model):
    uuid = models.CharField(max_length=36, default=generate_uuid, editable=False, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Movie(models.Model):
    uuid = models.CharField(max_length=36, default=generate_uuid, editable=False, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    genres = models.CharField(max_length=255)
    collection = models.ForeignKey(Collections, related_name='movies', on_delete=models.CASCADE)
