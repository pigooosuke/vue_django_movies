from django.core.management.base import BaseCommand

from ...models import Genre, Movie, User, Tag, UserTag, Rating

import csv
import pathlib
import urllib.request
import zipfile

# BaseCommandを継承して作成


class Command(BaseCommand):
    help = 'Add movie lens dataset'

    movielens_url = 'http://files.grouplens.org/datasets/movielens/'
    movielens_filename = "ml-latest-small.zip"
    movielens_extracted_folder = "ml-latest-small"
    download_dir = pathlib.Path('movies/data')

    def download(self, base_url, filename, download_dir):
        save_path = download_dir / filename
        if not save_path.exists():
            if not download_dir.exists():
                download_dir.mkdir(exist_ok=True)

            print("Downloading", filename, "...")

            # Download the file from the internet.
            url = base_url + filename
            file_path, _ = urllib.request.urlretrieve(url=url,
                                                      filename=str(save_path))

            print("Download finished. Extracting files.")

            if file_path.endswith(".zip"):
                # Unpack the zip-file.
                zipfile.ZipFile(file=file_path, mode="r").extractall(
                    download_dir)

            print("Done.")

    def handle(self, *args, **options):
        self.download(
            self.movielens_url,
            self.movielens_filename,
            self.download_dir)
        movies_csv = self.download_dir / self.movielens_extracted_folder / "movies.csv"
        ratings_csv = self.download_dir / self.movielens_extracted_folder / "ratings.csv"
        tags_csv = self.download_dir / self.movielens_extracted_folder / "tags.csv"
        links_csv = self.download_dir / self.movielens_extracted_folder / "links.csv"

        # load movies, genres
        movie_title_dict = dict()
        movie_genre_dict = dict()
        movie_imdb_dict = dict()
        movie_tmdb_dict = dict()
        genre_dict = dict()
        with open(str(movies_csv)) as f:
            next(f)
            contents = csv.reader(f, delimiter=",", quotechar='"')
            for content in contents:
                movie_id, title, genres = content
                splited_genres = genres.split("|")
                for genre in splited_genres:
                    if genre not in genre_dict:
                        genre_dict[genre] = len(genre_dict) + 1
                # set dict
                movie_title_dict[movie_id] = title
                genre_id_list = [genre_dict[genre] for genre in splited_genres]
                movie_genre_dict[movie_id] = genre_id_list

        with open(str(links_csv)) as f:
            next(f)
            contents = csv.reader(f, delimiter=",", quotechar='"')
            for content in contents:
                movie_id, imdb_id, tmdb_id = content
                movie_imdb_dict[movie_id] = imdb_id
                movie_tmdb_dict[movie_id] = tmdb_id

        # set model data
        movies = list()
        genres = list()
        for movie_id in movie_title_dict:
            movie = Movie(
                id=movie_id,
                name=movie_title_dict[movie_id],
                imdb_id=movie_imdb_dict[movie_id],
                tmdb_id=movie_tmdb_dict[movie_id])
            movies.append(movie)
        for movie_genre in genre_dict:
            genre = Genre(name=movie_genre)
            genres.append(genre)
        # bulk create movie/genre
        Movie.objects.bulk_create(movies)
        Genre.objects.bulk_create(genres)

        Through = Movie.genres.through
        throughs = list()
        for movie_id, genre_ids in movie_genre_dict.items():
            for genre_id in genre_ids:
                through = Through(movie_id=movie_id, genre_id=genre_id)
                throughs.append(through)
        # bulk create movie-genre relation
        Through.objects.bulk_create(throughs)

        # load ratings
        user_ids = set()
        ratings = list()
        with open(str(ratings_csv)) as f:
            next(f)
            contents = csv.reader(f, delimiter=",", quotechar='"')
            for content in contents:
                user_id, movie_id, rating, timestamp = content
                rating = Rating(user_id=user_id, movie_id=movie_id,
                                rating=rating, timestamp=timestamp)
                ratings.append(rating)
                user_ids.add(user_id)

        # load tags
        tags = list()
        user_tags = list()
        tag_dict = dict()
        with open(str(tags_csv)) as f:
            next(f)
            contents = csv.reader(f, delimiter=",", quotechar='"')
            for content in contents:
                user_id, movie_id, tag_name, timestamp = content
                if tag_name not in tag_dict:
                    tag_dict[tag_name] = len(tag_dict) + 1
                tag = Tag(name=tag_name)
                tags.append(tag)
                user_tags.append(
                    UserTag(
                        user_id=user_id,
                        tag_id=tag_dict[tag_name],
                        movie_id=movie_id,
                        timestamp=timestamp))
                user_ids.add(user_id)
        # user
        users = list()
        for user_id in user_ids:
            user = User(id=user_id)
            users.append(user)
        # bulk create user
        User.objects.bulk_create(users)
        Rating.objects.bulk_create(ratings)
        Tag.objects.bulk_create(tags)
        UserTag.objects.bulk_create(user_tags)

        print("command finished")
