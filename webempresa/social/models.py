from django.db import models

# Create your models here.

class Link(models.Model):
    key = models.SlugField(verbose_name="Nombre clave", max_length=100, unique=True)
    name = models.CharField(verbose_name="Red social", max_length=200)
    url = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación') ##fecha de creación, 
    updated =models.DateTimeField(auto_now=True, verbose_name='Fecha de edición') #Fecha de modificación

    class Meta:
        verbose_name = "enlace" #Para colocar otro nombre en el panel, por defecto seria el nombre de la clase Project
        verbose_name_plural = "enlaces" #simplemente para definir el nobre en plural.
        ordering = ["-name"] #el "-" hara que ordene del mas nuevo al mas antiguo, si el hara lo contrario.

    def __str__(self):
        return self.name #Para que en los proyectos, aparesca el titulo como nombre del proyecto.
