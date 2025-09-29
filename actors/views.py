from rest_framework import generics
from .models import Actor
from .serializers import ActorSerializer

class ActorListCreateView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()  # Define o conjunto de dados para a visualização
    serializer_class = ActorSerializer  # Define o serializador a ser usado

class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()  # Define o conjunto de dados para a visualização
    serializer_class = ActorSerializer  # Define o serializador a ser usado