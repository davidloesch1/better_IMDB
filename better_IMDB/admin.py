from django.contrib import admin
from .models import Movie, Role, Genre, Movie_Person, Movie_Person_Role

admin.site.register(Movie)
admin.site.register(Role)
admin.site.register(Genre)
admin.site.register(Movie_Person)
admin.site.register(Movie_Person_Role)
