from django.db import models

class Actor(models.Model):
	"""
	Model: Actor

	Field names:
	name: Actor name
	"""
	name = models.CharField(max_length=200)

	def __str__(self):
		return "{}".format(self.name)

	class Meta:
		ordering = ('name', )

class Movie(models.Model):
	"""
	Model: Actor

	Field names:
	title: Movie name
	actors: List of actors associated with the movie
	year: Year of movie
	"""
	title = models.CharField(max_length=200)
	actors = models.ManyToManyField(Actor)
	year = models.IntegerField()

	def __str__(self):
		return "{}".format(self.title)

	class Meta:
		ordering = ('title', )