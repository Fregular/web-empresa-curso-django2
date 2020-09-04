from django.contrib import admin
from .models import Category, Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title','author','published', 'post_categories') #campos a mostrar, no funciona con ManyToMany
    ordering = ('author', 'published') #ordenar
    search_fields = ('title','content','author__username','categories__name') #busquedas
    #author__username se agrega de esta forma, ya que viene de la tabla
    #de usuarios de django, por tanto se llama de esa forma.
    date_hierarchy = 'published'
    list_filter = ('author__username','categories__name') ##filtro

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorías"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)



