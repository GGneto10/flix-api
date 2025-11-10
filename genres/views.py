from rest_framework import generics
from .models import Genre
from .serializers import GenreSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import GenrePermissionClass
class GenreListCreateView(generics.ListCreateAPIView): 
    permission_classes = (IsAuthenticated, GenrePermissionClass,)
    queryset = Genre.objects.all() # Define o conjunto de dados para a visualização
    serializer_class = GenreSerializer # Define o serializador a ser usado

class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GenrePermissionClass,)
    queryset = Genre.objects.all() # Define o conjunto de dados para a visualização
    serializer_class = GenreSerializer # Define o serializador a ser usado