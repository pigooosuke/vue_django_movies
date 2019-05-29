import logging
import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from django.contrib.auth import models as auth_models
from graphene_django.filter import DjangoFilterConnectionField
from movies.models import Genre, Movie, User, Tag, UserTag, Rating

LOGGER = logging.getLogger(__name__)


class UserNode(DjangoObjectType):
    class Meta:
        model = auth_models.User
        exclude_fields = ('password')


class GenreNode(DjangoObjectType):
    class Meta:
        model = Genre
        filter_fields = ['name']
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


class Query(graphene.ObjectType):
    movie = relay.Node.Field(MovieNode)
    all_movies = DjangoFilterConnectionField(MovieNode)

    genre = relay.Node.Field(GenreNode)
    all_genres = DjangoFilterConnectionField(GenreNode)


"""
query {
    allMovies{
        id,
        name
    }
}

query {
    allMovies{
        id,
        name,
        genres {
            id,
            name
        }
    }
}

query {
    allGenres {
        edges {
            node {
                name
            }
        }
    }
}

query {
    allMovies(name_Icontains: "to") {
        edges {
            node {
                name
            }
        }
    }
}
"""
