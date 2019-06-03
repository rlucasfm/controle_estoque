from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'estoque'
urlpatterns = [
    path('', views.PaginaPrincipal, name='PaginaPrincipal'),
    path('modificarproduto/<int:id_produto>', views.ModificarProduto, name='ModificarProduto'),
    path('deletarproduto/<int:id_produto>', views.DeletarProduto, name='DeletarProduto'),
    path('adicionarprodutos/', views.AdicionarProduto, name='AdicionarProdutos'),
    path('exibirprodutos/', views.ExibirProdutos, name="ExibirProdutos"),
    path('exibirprodutos/<int:id_produto>', views.DetalheProdutos, name="Detalhes"),
]