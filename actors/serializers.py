from rest_framework import serializers
from .models import Actor

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'
    #Ou pode ser fields = ['id', 'name', 'birth_date', 'nationality']
    