from django.db import models
from actors.models import Actor
from genres.models import Genre


class Movie(models.Model):

    title = models.CharField(max_length=200)
    release_date = models.DateField(null=True, blank=True)
    Br_release_date = models.DateField(null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')
    resume = models.TextField(blank=True, null=True)


    #ManyToManyField -
    #Resumindo: um filme pode ter vários atores e um ator pode estar em vários filmes.
    def __str__(self):
        return self.title
