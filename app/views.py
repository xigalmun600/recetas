from django.shortcuts import render
from .models import Ingrediente, CategoriaIngrediente

# Create your views here.
def inicio(request):
    return render(request, 'app/inicio.html')

def ingredientes_lista(request):
    ingredientes = Ingrediente.objects.all()
    categorias = CategoriaIngrediente.objects.all()

    categoria_filtro = request.GET.get('categoria')

    if categoria_filtro:
        ingredientes = ingredientes.filter(categoria=categoria_filtro)

    return render(request, 'app/ingredientes_lista.html', {'categorias':categorias, 'ingredientes':ingredientes})