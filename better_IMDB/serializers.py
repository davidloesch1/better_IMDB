from rest_framework import serializers
from .models import Movie, Genre, Director, Actor
# from django.contrib.auth import get_user_model
# User = get_user_model()



class DirectorSerializer(serializers.ModelSerializer):

    director_url = serializers.ModelSerializer.serializer_url_field(
        view_name='director_detail'
    )

    movies = serializers.HyperlinkedRelatedField(
        view_name='movie_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Director
        fields = ('id', 'director_url', 'name',
                  'date_of_birth', 'country_of_birth', 'movies')


class ActorSerializer(serializers.ModelSerializer):

    actor_url = serializers.ModelSerializer.serializer_url_field(
        view_name='actor_detail'
    )

    movies = serializers.HyperlinkedRelatedField(
        view_name='movie_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Actor
        fields = ('id', 'actor_url', 'name',
                  'date_of_birth', 'country_of_birth', 'movies')


class GenreSerializer(serializers.ModelSerializer):

    genre_url = serializers.ModelSerializer.serializer_url_field(
        view_name='genre_detail'
    )

    movies = serializers.HyperlinkedRelatedField(
        view_name='movie_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Genre
        fields = ('id', 'genre_url', 'genre_description', 'movies',)


class MovieSerializer(serializers.ModelSerializer):
    directors = serializers.HyperlinkedRelatedField(
        view_name='director_detail',
        many=True,
        read_only=False,
        queryset=Director.objects.all()
    )

    actors = serializers.HyperlinkedRelatedField(
        view_name='actor_detail',
        many=True,
        read_only=False,
        queryset=Actor.objects.all()
    )

    genres = serializers.HyperlinkedRelatedField(
        view_name='genre_detail',
        many=True,
        read_only=False,
        queryset=Genre.objects.all()
    )

    movie_url = serializers.ModelSerializer.serializer_url_field(
        view_name='movie_detail'
    )

    class Meta:
        model = Movie
        fields = ('id', 'movie_url', 'title', 'plot_description',
                  'year_released', 'directors', 'actors', 'genres',)
