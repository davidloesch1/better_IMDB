from django.db import models


class Genre(models.Model):
    genre_description = models.CharField(max_length=100)

    def __str__(self):
        return self.genre_description


class Movie(models.Model):
    title = models.CharField(max_length=100)
    year_released = models.IntegerField()
    plot_description = models.TextField()
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE, related_name='movie')

    def __str__(self):
        return self.title


class Movie_Person(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    country_of_birth = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Role(models.Model):
    role_description = models.CharField(max_length=100)

    def __str__(self):
        return self.role_description


class Movie_Person_Role(models.Model):
    role_id = models.ForeignKey(
        Role, on_delete=models.CASCADE, related_name='movie_person_role')
    movie_id = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='movie_person_role')
    movie_person_id = models.ForeignKey(
        Movie_Person, on_delete=models.CASCADE, related_name='movie_person_role')

    def __str__(Role):
        return Role.role_description
