from rest_framework import serializers
from .models import Collections, Movie

class MovieSerializer(serializers.ModelSerializer):
    uuid = serializers.CharField(read_only=True)

    class Meta:
        model = Movie
        fields = ['uuid', 'title', 'description', 'genres']

class CollectionSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)

    class Meta:
        model = Collections
        fields = ['uuid', 'title', 'description', 'movies']

    def create(self, validated_data):
        movies_data = validated_data.pop('movies')
        collection = Collections.objects.create(**validated_data)
        for movie_data in movies_data:
            Movie.objects.create(collection=collection, **movie_data)
        return collection

    def update(self, instance, validated_data):
        movies_data = validated_data.pop('movies', None)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        if movies_data is not None:
            instance.movies.all().delete()
            for movie_data in movies_data:
                Movie.objects.create(collection=instance, **movie_data)

        return instance
