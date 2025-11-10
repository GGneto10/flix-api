from rest_framework import permissions

class GenrePermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
           return request.user.has_perm('genres.view_genre')
            # Permitir GET se o usuário tiver permissão de visualização.

        if request.method == 'POST':
            return request.user.has_perm('genres.add_genre')
             # Permitir POST se o usuário tiver permissão de adição.  

        if request.method in ['PUT', 'PATCH']:
            return request.user.has_perm('genres.change_genre')
             # Permitir PUT/PATCH se o usuário tiver permissão de alteração.
        

        if request.method == 'DELETE':
            return request.user.has_perm('genres.delete_genre')
             # Permitir DELETE se o usuário tiver permissão de exclusão.
    
        return False



