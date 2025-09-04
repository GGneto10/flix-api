from django.contrib import admin
from django.urls import path
from django.http import JsonResponse # Import HttpResponse for a simple view

def hello_world(request):
    return JsonResponse({'message':"Hello, World!"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),  # Add a simple view to the URL patterns   
]
