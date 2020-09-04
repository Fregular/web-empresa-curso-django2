from .models import Link


def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx
''' este processor permite agregar nuevos contextos custom,
para ser utilizados en los templates, ejemplo {{test}}. Este test
seria la clave de un diccionario. 

Para que django conozca el processor, se debe agregar en settings.
'''