from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TarefaManager(models.Manager):
    def search(self, query, user):
        return self.get_queryset().filter(
            models.Q(nome__icontains=query) | #busca por nome da tarefa, case not sensitive
            models.Q(descricao__icontains=query) | #busca por descricao da tarefa, case not sensitive
            models.Q(categoria__nome__icontains=query, user=user) #busca por nome da categoria, case not sensitive
        )


class Categoria(models.Model):
    nome = models.CharField(u'Nome', max_length=100)
    descricao = models.TextField(verbose_name='Descrição')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome;

class Tarefa(models.Model):
    PRIORIDADE_CHOICES = (
        ('B', 'Baixa'),
        ('M', 'Média'),
        ('A', 'Alta'),
    )
    STATUS_CHOICES = (
        ('C', 'Concluído'),
        ('CD', 'Cancelado')
    )
    nome = models.CharField(u'Nome', max_length=100)
    descricao = models.TextField(verbose_name='Descrição', blank=True)
    data_final = models.DateTimeField(u'Data final')
    prioridade = models.CharField(u'Prioridade', max_length=1, choices=PRIORIDADE_CHOICES)
    categoria = models.ForeignKey(Categoria,  verbose_name='Categoria', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    status = models.CharField(u'Status', max_length=5, choices=STATUS_CHOICES, blank=True, default='')

    objects = TarefaManager()

    def __str__(self):
        return self.nome;