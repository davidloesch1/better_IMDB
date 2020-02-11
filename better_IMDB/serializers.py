from rest_framework import serializers
from .models import Movie, Genre, Director, Actor


class DirectorSerializer(serializers.ModelSerializer):

    # movies = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all(), source='movies.id')

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

    # def create(self, validated_data):
    #     director = Director.objects.create(movie=validated_data['movie']['id'],
    #                                        name=validated_data['name'],
    #                                        date_of_birth=validated_data['date_of_birth'],
    #                                        country_of_birth=validated_data['country_of_birth'])
    #     return director


class MovieSerializer(serializers.ModelSerializer):
    directors = serializers.HyperlinkedRelatedField(
        view_name='director_detail',
        many=True,
        read_only=True
    )

    # directors = DirectorSerializer(many=True)

    # actors = serializers.HyperlinkedRelatedField(
    #     view_name = 'actor_detail',
    #     many = True,
    #     read_only = True
    # )

    # genre = serializers.HyperlinkedRelatedField(
    #     view_name = 'genre_detail',
    #     many = False,
    #     read_only = True
    # )

    movie_url = serializers.ModelSerializer.serializer_url_field(
        view_name='movie_detail'
    )

    class Meta:
        model = Movie
        fields = ('id', 'movie_url', 'title', 'plot_description',
                  'year_released', 'directors',)
