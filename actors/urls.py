from django.urls import path
from .views import ActorListCreateView, ActorRetrieveUpdateDestroyView 

urlpatterns = [
    path('actors/', ActorListCreateView.as_view(), name='actors-create-list'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-view'),
]