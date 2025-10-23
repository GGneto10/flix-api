from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

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