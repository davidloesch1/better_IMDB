from django.db import models


class Genre(models.Model):
    genre_description = models.CharField(max_length=100)

    def __str__(self):
        return self.genre_description


class Actor(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    country_of_birth = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Director(models.Model):
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
        Genre, on_delete=models.CASCADE, related_name='genre')
    directors = models.ManyToManyField(
        Director, related_name='movies')
    actors = models.ManyToManyField(
        Actor, related_name='movies')

    def __str__(self):
        return self.title
