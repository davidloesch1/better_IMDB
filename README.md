# better_IMDB

# Project Overview

## Project Description
Movie database API which allows full CRUD actions on some of the models.  A key aspect of this database is that it utilizes the ManyToManyField functionality on Django to refer multiple movies to multiple actors and vice versa.  Additionally this backend is built using Django REST Framework.

## Project Links
- [repo] (https://github.com/lilspikey333/better_IMDB)

## Setup Instructions
- Clone down the repo and `cd` into the local repo
- Activate a python virtual environment
- Set up the Postgres db
    - `CREATE DATABASE better_imdb;`
    - `CREATE USER imdbuser WITH PASSWORD 'password'`;
    - `GRANT ALL PRIVILEGES ON DATABASE better_imdb TO imdbuser`;
- Run the migrate command (`python3 manage.py migrate`)
- Create superuser (`python3 manage.py createsuperuser`)
- Start the server

## Models
- Movie
    - title
    - year_released
    - plot_description
    - genre (fk)
    - director(s) (fk)
    - actor(s) (fk)

- Genre
    - genre_description

- Actor
    - name
    - dob
    - country_of_birth

- Director
    - name
    - dob
    - country_of_birth


## Next Steps
     - Build a front-end to utilize the database
     - Front-end can be similar to IMDB
     - Include photos for the movies, directors, and actors
     - Anything else you can think of!