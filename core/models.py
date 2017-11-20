from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Aluno(models.Model):
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		blank=True,
		null=True,
		limit_choices_to={'groups__name': "Alunos"},
		related_name='aluno')
	def __str__(self):              
		return self.user.username

class Avaliador(models.Model):
	user = models.OneToOneField(User,
		on_delete=models.CASCADE,
		blank=True,
		null=True,
		limit_choices_to={'groups__name': "Avaliadores"},
		related_name = 'avaliador')
	def __str__(self):              
		return self.user.username

class Projeto(models.Model):
	nome = models.CharField("Nome", max_length=120)
	resumo = models.TextField("Resumo", blank=True, null=True)
	aluno = models.ManyToManyField("Aluno")
	avaliador = models.ManyToManyField("Avaliador")

	def __str__(self):              
		return self.nome

	class Meta:
		 ordering = ('nome',)

class Avaliacao(models.Model):

	projeto = models.ForeignKey(Projeto,blank=True,null=True)
	avaliador = models.ForeignKey(Avaliador,blank=True,null=True)
	estrelas = models.PositiveIntegerField("Estrelas",blank=True,null=True)
	nota = models.PositiveIntegerField("Nota", blank=True, null=True)
	alunos_sem_camisa = models.PositiveIntegerField("Alunos sem camiseta do porteira", default=0)
	ocorrencias = models.TextField("Ocorrências", blank=True, null=True)

