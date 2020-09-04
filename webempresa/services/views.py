from django.shortcuts import render
from .models import Project

# Create your views here.
def services(request):
    projects = Project.objects.all()  #esta consulta, trae todos los projectos de la base
    return  render(request, "services/services.html",{'projects':projects}) #aca pasamos los proyectos, a la views, el resultado podriamos ver en el
    #template portfolio.html con {{project}} por ejemplo, esta es el resultado de la query, y puede ser visualizada para trabajar con ella.