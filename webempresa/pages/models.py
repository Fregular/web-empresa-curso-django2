from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Pages(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación') ##fecha de creación, 
    updated =models.DateTimeField(auto_now=True, verbose_name='Fecha de edición') #Fecha de modificación

    class Meta:
        verbose_name = "página" #Para colocar otro nombre en el panel, por defecto seria el nombre de la clase Project
        verbose_name_plural = "páginas" #simplemente para definir el nobre en plural.
        ordering = ['order','-title'] #el "-" hara que ordene del mas nuevo al mas antiguo, si el hara lo contrario.

    def __str__(self):
        return self.title #Para que en los proyectos, aparesca el titulo como nombre del proyecto.
