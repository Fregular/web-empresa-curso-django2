from django.contrib import admin

# Register your models here.
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    '''
    Aca, creamos una clase con cualquier nombre, pero le pasamos admin.ModelAdmin, y definimos
    2 campos que vienen del models.py, para que se incorporen en el admin como solo lectura.
    '''
    readonly_fields = ('created','updated')

admin.site.register(Project, ProjectAdmin)