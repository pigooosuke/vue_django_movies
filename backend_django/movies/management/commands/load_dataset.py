from django.core.management.base import BaseCommand

from ...models import Genre, Movie, Age, Occupation, User, Rate

import pandas as pd
from itertools import chain

# BaseCommandを継承して作成


class Command(BaseCommand):
    help = 'Add movie lens dataset'

    def handle(self, *args, **options):
        # load movies, genres
        movies = list()
        genres = list()
        df = pd.read_csv("movies.dat", encoding="windows-1252", delimiter="::",
                         names=["movie_id", "title", "genres"], engine="python")
        splited_genres = df['genres'].str.split('|')
        df_movies = pd.DataFrame({
            'title': df['title'].values.repeat(splited_genres.str.len()),
            'genres': list(chain.from_iterable(splited_genres.tolist()))
        })
        del df

        for movie_title in df_movies["title"].unique():
            movie = Movie(title=movie_title)
            movies.append(movie)
        for movie_genre in df_movies["genres"].unique():
            genre = Genre(name=movie_genre)
            genres.append(genre)
        # bulk create movie/genre
        Movie.objects.bulk_create(movies)
        Genre.objects.bulk_create(genres)

        title_labels, _ = pd.factorize(df_movies["title"])
        genre_labels, _ = pd.factorize(df_movies["genres"])

        Through = Movie.genres.through
        through_list = []
        for l, g in zip(title_labels, genre_labels):
            through_list.append(Through(movie_id=l+1, genre_id=g+1))
        # bulk create movie-genre relation
        Through.objects.bulk_create(through_list)

        # load ratings
        with open("ratings.dat", "r") as f:
            for l in f:
                row = l.strip().split("::")
                rate_user_id = row[0]
                rate_movie_id = row[1]
                rate_rate = row[2]
                rate_timestamp = row[3]
        # users
        with open("users.dat", "r") as f:
            for l in f:
                row = l.strip().split("::")
                user_id = row[0]
                user_gender = row[1]
                user_age = row[2]
                user_occupation = row[3]
                user_zipcode = row[4]
