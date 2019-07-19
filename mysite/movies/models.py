from django.db import models

# Create your models here.
class Actor(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return "{}".format(self.name)

	class Meta:
		ordering = ('name', )

class Movie(models.Model):
	title = models.CharField(max_length=200)
	actors = models.ManyToManyField(Actor)
	year = models.IntegerField()

	def __str__(self):
		return "{}".format(self.title)

	class Meta:
		ordering = ('title', )