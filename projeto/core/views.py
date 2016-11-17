from django.shortcuts import render
from projeto.core.forms import Operacao
from django.http import HttpResponse  
from projeto.core.models import Resultado

from projeto.core.operacao import soma


# Create your views here.

def calculo(request):

	form = Operacao(request.POST)
	if form.is_valid():
		resultado = soma(form.cleaned_data['numero_um'], form.cleaned_data['numero_dois'])
		res = Resultado()
		res.resultado = resultado
		res.save()
	context = {'form': form}

	return render(request, 'calculo.html', context)


def resultado(request):
	return render(request, 'resultado.html')	


