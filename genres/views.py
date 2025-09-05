from django.http import JsonResponse
from .models import Genre

def genre_view(request):
    genres = Genre.objects.all()
    data = [{"id": genre.id, "name": genre.name} for genre in genres]
    #Isso aqui apenas existe pois o JsonResponse não aceita QuerySets diretamente
    #E pq eu não estou usando Django Rest Framework.

    return JsonResponse(data, safe=False)
    #Retorna uma lista de generos em formato JSON

    #Safe False é necessário para retornar listas
    #Por padrão, JsonResponse só aceita dicionários