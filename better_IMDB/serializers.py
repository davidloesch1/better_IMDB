from rest_framework import serializers
from .models import Movie, Genre, Director, Actor

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    directors = serializers.HyperlinkedRelatedField(
        view_name = 'director_detail',
        many = True,
        read_only = True
    )

    actors = serializers.HyperlinkedRelatedField(
        view_name = 'actor_detail',
        many = True,
        read_only = True
    )

    genre = serializers.HyperlinkedRelatedField(
        view_name = 'genre_detail',
        many = False,
        read_only = True
    )

    class Meta:
        model = Movie
        fields = ('id', 'directors', 'actors', 'genre', 'title', 'plot_description', 'year_released',)