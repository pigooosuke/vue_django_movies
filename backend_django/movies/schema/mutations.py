import logging
import graphene
from movies.models import Genre, Movie, User, Tag, UserTag, Rating
from graphql_relay.node.node import from_global_id
from . import model_mutations, queries

LOGGER = logging.getLogger(__name__)




class Mutation:
    pass
