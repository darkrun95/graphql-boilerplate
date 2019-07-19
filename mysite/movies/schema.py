import graphene

from graphene_django.types import DjangoObjectType, DjangoObjectType
from movies.models import *

class ActorType(DjangoObjectType):
	class Meta:
		model = Actor

class MovieType(DjangoObjectType):
	class Meta:
		model = Movie