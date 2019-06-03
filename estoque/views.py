from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Produto
from .forms import FormProdutos



def PaginaPrincipal(request):
    return render(request, 'estoque/paginaprincipal.html')

def ExibirProdutos(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos,
    }

    try:
        nome_pesquisado = request.POST['nome']

        if nome_pesquisado:
            prodpesquisa = Produto.objects.get(nome = nome_pesquisado)
            return redirect(reverse('estoque:Detalhes', args=(prodpesquisa.id,)))


    except(KeyError):
        return render(request, 'estoque/exibirprodutos.html', context)
    except(Produto.DoesNotExist):
        context['erro'] = "Não existe nenhum produto com este nome."
        return render(request, 'estoque/exibirprodutos.html', context)

    else:
        return HttpResponseRedirect(reverse('estoque:ExibirProdutos'))

def DetalheProdutos(request, id_produto):
    produto = Produto.objects.get(pk=id_produto)
    context ={
        'produto': produto,
    }
    return render(request, 'estoque/detalhes.html', context)

def AdicionarProduto(request):
    form = FormProdutos(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('estoque:ExibirProdutos')

    return render(request, 'estoque/adicionarproduto.html', {'form': form})

def ModificarProduto(request, id_produto):
    produto = Produto.objects.get(pk=id_produto)
    form = FormProdutos(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('estoque:ExibirProdutos')

    context={
        'form': form
    }
    return render(request, 'estoque/modificarproduto.html', context)

def DeletarProduto(request, id_produto):
    prod = Produto.objects.get(pk=id_produto)
    prod.delete()
    return redirect('estoque:ExibirProdutos')

