from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Projeto, Avaliador, Avaliacao
from django.shortcuts import render, get_object_or_404
from .forms import AvaliacaoForm
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Alunos').count() == 0, login_url='/')
def projetos_list(request):
	projetos = Projeto.objects.filter(avaliador__user__id = request.user.id)
	return render(request, 'core/projetos_list.html',{'projetos':projetos})

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Alunos').count() == 0, login_url='/')
def projeto_detalhe(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    avaliadores = Avaliador.objects.filter(user__id=request.user.id)
    avaliador = avaliadores[0]
    avaliacoes =Avaliacao.objects.filter(avaliador__user__id=request.user.id).filter(projeto__pk=pk)
    try:
    	avaliacao = avaliacoes[0]
    	nota = avaliacao.nota
    	alunos_sem_camisa = avaliacao.alunos_sem_camisa
    	estrelas = avaliacao.estrelas
    except:
    	avaliacao = Avaliacao()
    	avaliacao.projeto = projeto
    	avaliacao.avaliador = avaliador
    	nota = 0
    	alunos_sem_camisa = 0
    	estrelas = 0
    avaliacao.nota = nota
    avaliacao.alunos_sem_camisa = alunos_sem_camisa
    avaliacao.estrelas = estrelas
    avaliacao.save()
    return render(request, 'core/projeto_detalhe.html', {
    	'projeto': projeto,
    	'avaliador':avaliador,
    	'nota':nota,
    	'alunos_sem_camisa' : alunos_sem_camisa,
    	'estrelas' : estrelas,
    	'avaliacao': avaliacao
    	})

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Alunos').count() == 0, login_url='/')
def projeto_avaliar(request, pk):
	avaliacao = get_object_or_404(Avaliacao, pk=pk)

	if request.method == "POST":
		form = AvaliacaoForm(request.POST, instance=avaliacao)
		if form.is_valid():
			avaliacao = form.save(commit=False)
			avaliacao.save()
			return redirect('projetos_list')
	else:
		print("merda")
		form = AvaliacaoForm(instance=avaliacao)
	return render(request, 'core/projeto_avaliar.html', {'form': form})