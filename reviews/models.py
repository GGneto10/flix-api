from django.db import models
from movies.models import Movie

from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(   
        validators=[
        MinValueValidator(0, 'Avaliação NÃO pode ser inferior a mínima que é 0.'),
        MaxValueValidator(5, 'Avaliação NÃO pode ser superior a máxima que é 5.'),
        ]   
    ) 
    comment = models.TextField(blank=True, null=True)
#A Reviews está vinculada a um Movie específico por meio de uma ForeignKey.
    def __str__(self):
        return f'Review for {self.movie.title} - {self.stars} stars'