from rest_framework import serializers
from .models import Movie
from django.db.models import Avg
class MovieSerializer(serializers.ModelSerializer):

    rate = serializers.SerializerMethodField(read_only=True) # -> Campo calculado dinamicamente

    class Meta:
        model = Movie
        fields = '__all__'
    
    def get_rate(self, obj):#o obj representa a instância do Movie atual
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        #NA aula 147 explica esse código.
        if rate:
            return round(rate, 2)
        
        return None
    # Outra forma de calcular a média das avaliações sem usar aggregate
        '''reviews = obj.reviews.all()  # Acessa todas as avaliações relacionadas ao filme
        
        if reviews:
            sum_revierws = 0

            for review in reviews:
                sum_revierws += review.stars
            
            reviews_count = reviews.count()

            return round(sum_revierws / reviews_count, 2)  # Retorna a média das avaliações
            

        return None # Retorna None se não houver avaliações
        '''

   

    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError("'Release date' deve ser apartir 1990 ou mais recente.")
        return value
    
    def validate_resume(self, value):
        if len(value) < 20:
            raise serializers.ValidationError("'Resume' deve conter pelo menos 20 caracteres.")
        return value
#Serializer - Resumindo: é uma forma de converter dados complexos, como objetos de banco de dados,

#Nos Serializers, podemos definir regras de validação personalizadas para garantir que os dados atendam a certos critérios antes de serem salvos no banco de dados.
# em formatos mais simples, como JSON ou XML, que podem ser facilmente transmitidos pela web.