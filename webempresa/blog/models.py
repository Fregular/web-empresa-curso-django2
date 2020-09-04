from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User ##todos los usuarios del panel de administrador

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated =models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = "categoría" #Para colocar otro nombre en el panel, por defecto seria el nombre de la clase Project
        verbose_name_plural = "categorías" #simplemente para definir el nobre en plural.
        ordering = ["-created"] #el "-" hara que ordene del mas nuevo al mas antiguo, si el hara lo contrario.

    def __str__(self):
        return self.name #Para que en los proyectos, aparesca el titulo como nombre del proyecto.


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publiación",default=now)
    image = models.ImageField(verbose_name="Image", upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE) ##el on_delete=models.CASCADE lo que hace 
    #es si un usuario es borrado, todos las entradas que haya generado se borraran tambien. Existe una opción llamada protected
    #que impide que se borre, pero quedaran entradas sin autor, por lo tante se recomienda agregar el null=True, blank=True
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_posts") #para traer los datos de Categorys, ya que son muchas las opciones.

    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated =models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = "entrada" #Para colocar otro nombre en el panel, por defecto seria el nombre de la clase Project
        verbose_name_plural = "entradas" #simplemente para definir el nobre en plural.
        ordering = ["-created"] #el "-" hara que ordene del mas nuevo al mas antiguo, si el hara lo contrario.

    def __str__(self):
        return self.title #Para que en los proyectos, aparesca el titulo como nombre del proyecto.
