import logging
import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from movies.models import Genre, Movie, User, Tag, UserTag, Rating

LOGGER = logging.getLogger(__name__)


class GenreNode(DjangoObjectType):
    class Meta:
        model = Genre
        filter_fields = ['name']
        interfaces = (relay.Node, )


class RatingNode(DjangoObjectType):
    class Meta:
        model = Rating
        interfaces = (relay.Node, )


class MovieNode(DjangoObjectType):
    class Meta:
        model = Movie
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'genres': ['exact'],
            'genres__name': ['exact'],
        }
        interfaces = (relay.Node, )

    genres = graphene.List(graphene.NonNull(GenreNode), required=True)

    @staticmethod
    def resolve_genres(movie, info):
        return movie.genres.all()


class Query(graphene.ObjectType):
    movie = relay.Node.Field(MovieNode)
    allMovies = DjangoFilterConnectionField(MovieNode)

    genre = relay.Node.Field(GenreNode)
    allGenres = DjangoFilterConnectionField(GenreNode)
