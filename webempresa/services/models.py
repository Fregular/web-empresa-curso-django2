from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    subtitle = models.CharField(max_length=200, verbose_name='Subtitulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name="Imagen", upload_to="projects") 
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación') ##fecha de creación, 
    updated =models.DateTimeField(auto_now=True, verbose_name='Fecha de edición') #Fecha de modificación

    class Meta:
        verbose_name = "servicio" #Para colocar otro nombre en el panel, por defecto seria el nombre de la clase Project
        verbose_name_plural = "servicios" #simplemente para definir el nobre en plural.
        ordering = ["-created"] #el "-" hara que ordene del mas nuevo al mas antiguo, si el hara lo contrario.

    def __str__(self):
        return self.title #Para que en los proyectos, aparesca el titulo como nombre del proyecto.