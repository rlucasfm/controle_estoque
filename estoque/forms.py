from django import forms
from .models import Produto

class FormProdutos(forms.ModelForm):

    class Meta:
        model = Produto
        fields =['nome', 'quantidade', 'valor']

