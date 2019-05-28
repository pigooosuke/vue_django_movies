from django.core.management.base import BaseCommand

from ...models import Genre, Movie, User, Tag, UserTag, Rating

import pandas as pd
import numpy as np
from itertools import chain

# BaseCommandを継承して作成


class Command(BaseCommand):
    help = 'Add movie lens dataset'

    def handle(self, *args, **options):
        # load movies, genres
        movies = list()
        genres = list()
        df_movies = pd.read_csv("movies.csv")
        splited_genres = df_movies['genres'].str.split('|')
        df_movies_repeat = pd.DataFrame({
            'movieId': df_movies['movieId'].values.repeat(splited_genres.str.len()),
            'genres': list(chain.from_iterable(splited_genres.tolist()))
        })

        for movie_id, movie_title in zip(df_movies["movieId"].values, df_movies["title"].values):
            movie = Movie(id=movie_id, title=movie_title)
            movies.append(movie)
        for movie_genre in df_movies_repeat["genres"].unique():
            genre = Genre(name=movie_genre)
            genres.append(genre)
        # bulk create movie/genre
        Movie.objects.bulk_create(movies)
        Genre.objects.bulk_create(genres)

        genre_labels, _ = pd.factorize(df_movies_repeat["genres"])

        Through = Movie.genres.through
        through_list = []
        for l, g in zip(df_movies_repeat["movieId"].values, genre_labels):
            through_list.append(Through(movie_id=l, genre_id=g+1))
        # bulk create movie-genre relation
        Through.objects.bulk_create(through_list)

        # load ratings, tags
        df_ratings = pd.read_csv("ratings.csv")
        df_tags = pd.read_csv("tags.csv")
        # user
        users = list()
        user_ids = np.unique(np.concatenate(
            (df_ratings["userId"].unique(), df_tags["userId"].unique()), 0))
        for user_id in user_ids:
            user = User(id=user_id)
            users.append(user)
        # bulk create user
        User.objects.bulk_create(users)

        # ratings
        ratings = list()
        for user_id, movie_id, rating, timestamp in zip(df_ratings["userId"].values, df_ratings["movieId"].values, df_ratings["rating"].values, df_ratings["timestamp"].values):
            rating = Rating(user_id=user_id, movie_id=movie_id,
                          rating=rating, timestamp=timestamp)
            ratings.append(rating)
        # bulk create ratings
        Rating.objects.bulk_create(ratings)

        # tags
        tags = list()
        for tag_name in df_tags["tag"].unique():
            tag = Tag(name=tag_name)
            tags.append(tag)
        # bulk create tag
        Tag.objects.bulk_create(tags)

        tag_labels, _ = pd.factorize(df_tags["tag"])

        usertags = []
        for user_id, movie_id, tag_id, timestamp in zip(df_tags["userId"].values, df_tags["movieId"].values, tag_labels, df_tags["timestamp"].values):
            usertags.append(UserTag(user_id=user_id, tag_id=tag_id+1, movie_id=movie_id, timestamp=timestamp))
        # bulk create movie-genre relation
        UserTag.objects.bulk_create(usertags)

        print("loaded dataset")