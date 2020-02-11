from rest_framework import generics
from .serializers import MovieSerializer, DirectorSerializer
from .models import Movie, Director, Actor, Genre

class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# class ActorList(generics.ListCreateAPIView):
#     queryset = Actor.objects.all()
#     serializer_class = ActorSerializer

# class ActorDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Actor.objects.all()
#     serializer_class = ActorSerializer

class DirectorList(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

# class GenreList(generics.ListCreateAPIView):
#     queryset = Genre.objects.all()
#     serializer_class = GenreSerializer

# class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Genre.objects.all()
#     serializer_class = GenreSerializer