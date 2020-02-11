# better_IMDB

# Project Overview

## Project Description
Movie database API which allows full CRUD actions on some of the models.  A key aspect of the database model is that a person's role on a movie is not stored on the movie directly, but in a "join" table which associates people, movies and roles.

## Project Links
- [repo] (https://github.com/lilspikey333/better_IMDB)

## Setup Instructions
- Clone down the repo and `cd` into the local repo
- Activate a python virtual environment
- Set up the Postgres db
    - `CREATE DATABASE better_imdb;`
    - `CREATE USER imdbuser WITH PASSWORD 'password'`;
    - `GRANT ALL PRIVILEGES ON DATABASE better_imdb TO imdbuser`;
- Start the server



## Models
- Movie
    - title
    - year_released
    - plot_description
    - genre (fk)

- Genre
    - genre_description

- Movie_Person
    - name
    - dob
    - country_of_birth

- Role
    - role_description

- Movie_Person_Role
    - role_id (fk)
    - movie_id (fk)
    - movie_person_id (fk)


## Routes