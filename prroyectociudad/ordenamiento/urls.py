from django.urls import path
# se importa las vistas de la aplicación
from . import views

urlpatterns = [
        path('listado/barrios', views.listadoBarrios,
            name='listadoBarrios'),
        path('crear/Barrio/<int:id>', 
            views.crearBarrio, 
            name='crearBarrio'),
        path('editarBarrio/<int:id>', views.editarBarrio, 
            name='editarBarrio'),
        path('eliminar/barrio/<int:id>', views.eliminarBarrio, 
            name='eliminarBarrio'),
        path('listado/parroquias', views.listadoParroquias, 
            name='listadoParroquias'),
        path('crear/parroquia', views.crearParroquia, 
            name='crearParroquia'),    
        path('editarParroquia/<int:id>', views.editarParroquia, 
            name='editarParroquia'),
 ]
