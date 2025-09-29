from django.contrib import admin
from actors.models import Actor

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'birth_date', 'nationality']  # Define os campos a serem exibidos na lista
    search_fields = ['name',]  # Adiciona campos de busca
