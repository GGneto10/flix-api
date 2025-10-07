from django.urls import path
from .views import MovieListCreateView, MovieRetrieveUpdateDestroyView    

urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='movies-create-list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail-view'),
]