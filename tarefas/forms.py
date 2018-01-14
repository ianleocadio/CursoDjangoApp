from django import forms
from .models import Categoria, Tarefa
from material import *

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        exclude = ('user',)
        #fields = ('nome', 'descricao') || ['nome', 'descricao']
        #exclude = ('descricao',) || ['descricao']

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        exclude = ('user',)
        widgets = {
            'data_final': forms.DateTimeInput,
            'descricao': forms.Textarea
        }
    def __init__(self, user=None, editing=False, *args, **kwargs):
        super(TarefaForm, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields['categoria'].queryset = Categoria.objects.filter(user=user)
        if not editing:
            self.fields['status'].widget = forms.HiddenInput()