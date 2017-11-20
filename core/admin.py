from django.contrib import admin
from .models import Avaliacao, Projeto, Aluno, Avaliador

# Register your models here.
admin.site.register(Avaliacao)
admin.site.register(Projeto)
admin.site.register(Aluno)
admin.site.register(Avaliador)