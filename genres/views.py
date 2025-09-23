from rest_framework import generics
from .models import Genre
from .serializers import GenreSerializer

class GenreListCreateView(generics.ListCreateAPIView): 
    queryset = Genre.objects.all() # Define o conjunto de dados para a visualização
    serializer_class = GenreSerializer # Define o serializador a ser usado

class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all() # Define o conjunto de dados para a visualização
    serializer_class = GenreSerializer # Define o serializador a ser usado