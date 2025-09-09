from django.http import JsonResponse
from .models import Genre
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json

@csrf_exempt
def genre_create_list_view(request):

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
    

@csrf_exempt
def genre_detail_view(request, pk):

    genre = get_object_or_404(Genre, pk=pk)
    if request.method == 'GET': # Retorna os detalhes de um gênero específico
        data = {"id": genre.id, "name": genre.name} # Dados do gênero
        return JsonResponse(data) # Retorna os dados em formato JSON
    
    elif request.method == 'PUT':   
        data = json.loads(request.body.decode('utf-8')) # Decodifica o corpo da requisição
        genre.name = data['name'] # Atualiza o nome do gênero
        genre.save() # Salva as alterações no banco de dados
        return JsonResponse({"id": genre.id, "name": genre.name}, # Retorna os dados atualizados
                            status=200)
