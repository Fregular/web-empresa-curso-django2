from django.urls import path
from . import views 


urlpatterns = [
    path('<int:page_id>/<slug:page_slug>/', views.page, name="page"),    

]


'''
El category_id es la primari key de la tabla.
Para ellos se crea un views category para manejar
los id de category. El int: convierte el dato en entero.
'''