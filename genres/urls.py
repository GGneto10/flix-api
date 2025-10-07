from django.urls import path
from .views import GenreListCreateView, GenreRetrieveUpdateDestroyView

urlpatterns = [
    path('genres/', GenreListCreateView.as_view(), name='reviews-create-list'),
    path('genres/<int:pk>/', GenreListCreateView.as_view(), name='review-detail-view'),
] 