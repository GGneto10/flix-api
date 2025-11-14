from rest_framework import generics
from .models import Actor
from .serializers import ActorSerializer
from rest_framework.permissions import IsAuthenticated # Importa a classe de permissão
from app.permissions import GlobalDefaultPermission

class ActorListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)  # Aplica a permissão de autenticação
    queryset = Actor.objects.all()  # Define o conjunto de dados para a visualização
    serializer_class = ActorSerializer  # Define o serializador a ser usado

class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Actor.objects.all()  # Define o conjunto de dados para a visualização
    serializer_class = ActorSerializer  # Define o serializador a ser usado