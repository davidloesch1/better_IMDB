from django.contrib import admin
from .models import Movie, Genre, Movie_Person

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Movie_Person)
