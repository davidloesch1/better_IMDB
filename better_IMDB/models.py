from django.db import models


class Genre(models.Model):
    genre_description = models.CharField(max_length=100)

    def __str__(self):
        return self.genre_description

class Movie_Person(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    country_of_birth = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year_released = models.IntegerField()
    plot_description = models.TextField()
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE, related_name='movie')
    directors = models.ForeignKey(
        Movie_Person, on_delete=models.CASCADE, related_name='movie')
    cast = models.ForeignKey(
        Movie_Person, on_delete=models.CASCADE, related_name='director')

    def __str__(self):
        return self.title