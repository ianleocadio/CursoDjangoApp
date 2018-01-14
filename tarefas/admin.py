from django.contrib import admin

# Register your models here.
from tarefas.models import Categoria, Tarefa


class CategoriaAdmin(admin.ModelAdmin):
    pass

class TarefaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Tarefa, TarefaAdmin)
