from django.http import JsonResponse
from .models import Genre
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def genre_view(request):

    if request.method == 'GET':
        genres = Genre.objects.all()
        data = [{"id": genre.id, "name": genre.name} for genre in genres]
        #Isso aqui apenas existe pois o JsonResponse não aceita QuerySets diretamente
        #E pq eu não estou usando Django Rest Framework.

        return JsonResponse(data, safe=False)
        #Retorna uma lista de generos em formato JSON
        #Safe False é necessário para retornar listas
        #Por padrão, JsonResponse só aceita dicionários

    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genre(name=data.get('name'))
        new_genre.save() 
        return JsonResponse({"id": new_genre.id, "name": new_genre.name}, status=201)
        #Esse 201 indica que um recurso foi criado com sucesso"
        #Sexosão POST para criar um novo gênero

         #Decodifica o corpo da requisição

        #Aqui você pode adicionar lógica para criar um novo gênero
        