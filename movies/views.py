from rest_framework import generics, views
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from django.db.models import Avg
from rest_framework.response import Response

class MovieListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()


    def get(self, request, format=None):
        total_movies = Movie.objects.count()
        average_rating = Movie.objects.aggregate(Avg('rating'))['rating__avg']
        stats = {
            'total_movies': total_movies,
            'average_rating': average_rating,
        }
        return Response(stats)