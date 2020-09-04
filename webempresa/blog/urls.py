from django.urls import path
from . import views 


urlpatterns = [
    path('', views.blog, name="blog"),
    path('category/<int:category_id>', views.category, name="category"),    

]


'''
El category_id es la primari key de la tabla.
Para ellos se crea un views category para manejar
los id de category. El int: convierte el dato en entero.
'''