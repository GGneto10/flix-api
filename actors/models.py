from django.db import models


NATIONALITY_CHOICES = [
    ('US', 'United States'),
    ('UK', 'United Kingdom'),
    ('CA', 'Canada'),
    ('AU', 'Australia'),
    ('FR', 'France'),
    ('DE', 'Germany'),
    ('IN', 'India'),
    ('JP', 'Japan'),
    ('BR', 'Brazil'),
    ('MX', 'Mexico'),
    ('IT', 'Italy'),
    ('ES', 'Spain'),
    ('RU', 'Russia'),
    ('CN', 'China'),
    ('KR', 'South Korea'),
    ('SE', 'Sweden'),
    ('NL', 'Netherlands'),
    ('NO', 'Norway'),
    ('DK', 'Denmark'),
    ('FI', 'Finland'),
]
#Configuração do modelo Actor com campos para nome, data de nascimento 
# e nacionalidade com Choices.
class Actor(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=2, choices=NATIONALITY_CHOICES, blank=True, null=True)
    
    def __str__(self):
        return self.name
