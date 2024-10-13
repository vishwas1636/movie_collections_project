from django.contrib.auth.models import User
from django.core.cache import cache
from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Collections, Movie
from .serializers import CollectionSerializer
from .services import fetch_movies
from collections import Counter

# user registration view
class Register(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
# Custom token view for JWT authentication
class GetToken(TokenObtainPairView):
    pass

# Pagination settings for movies, showing 10 per page
class MoviePagination(PageNumberPagination):
    page_size = 10

# Function to list movies from an external API
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_movie_list(request):
    page_number = request.query_params.get('page', 1)
    result = fetch_movies(page=page_number)
    if "error" in result:
        return Response({"error": result["error"]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    paginator = MoviePagination()
    paginated_result = paginator.paginate_queryset(result.get("results", []), request)
    return paginator.get_paginated_response(paginated_result)

# Function to get user's collections and top 3 favorite genres
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_my_collections(request):
    collections = Collections.objects.filter(user=request.user)
    genres_count = Counter()
    for collection in collections:
        for movie in collection.movies.all():
            genres_list = movie.genres.split(", ")
            genres_count.update(genres_list)
    
    # Get the top 3 genres
    top_3_genres = [genre for genre, count in genres_count.most_common(3)]
    favourite_genres = ", ".join(top_3_genres)
    
    response_data = {
        "is_success": True,
        "data": {
            "collections": CollectionSerializer(collections, many=True).data,
            "favourite_genres": favourite_genres
        }
    }
    return Response(response_data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def collections_get_or_add(request):
    if request.method == 'GET':
        collections = Collections.objects.filter(user=request.user)
        genres_count = Counter()
        for collection in collections:
            for movie in collection.movies.all():
                genres_list = movie.genres.split(", ")
                genres_count.update(genres_list)
        
        # Get the top 3 genres
        top_3_genres = [genre for genre, count in genres_count.most_common(3)]
        favourite_genres = ", ".join(top_3_genres)
        
        response_data = {
            "is_success": True,
            "data": {
                "collections": CollectionSerializer(collections, many=True).data,
                "favourite_genres": favourite_genres
            }
        }
        return Response(response_data)

    elif request.method == 'POST':
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            collection = serializer.save(user=request.user)
            return Response({"collection_uuid": collection.uuid}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# this function is used for retrieving, updating, and deleting collections
class Collectionedit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collections.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'uuid'

    def get_queryset(self):
        return Collections.objects.filter(user=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        

        # Handle updating movies if provided
        movies_data = request.data.get('movies', None)
        if movies_data is not None:
            instance.movies.all().delete()
            for movie_data in movies_data:
                Movie.objects.create(collection=instance, **movie_data)
        
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        movies = instance.movies.all()
        movies_data = [{"title": movie.title, "description": movie.description, "genres": movie.genres, "uuid": movie.uuid} for movie in movies]
        return Response({
            "title": serializer.data['title'],
            "description": serializer.data['description'],
            "movies": movies_data
        })

# get the count of requests
@api_view(['GET'])
def get_request_count(request):
    count = cache.get('request_count', 0)
    return Response({'requests': count})

# resetting the request count
@api_view(['POST'])
def reset_request_count(request):
    cache.set('request_count', 0)
    return Response({'message': 'Request count reset successfully'})
