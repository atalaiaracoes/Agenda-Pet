from django.shortcuts import render, redirect
from .models import Servico
from .forms import CadastroServico


def lista_servico(request):
	servico = Servico.objects.all()
	context = {'servico': servico}
	return render(request, 'lista_servico.html', context)


def cadastro_servico(request):
	servico_id = request.GET.get('id')

	if servico_id:
		altservico = Servico.objects.get(id=servico_id)
		return render(request, 'cadastro_servico.html', {'altservico': altservico})

	if request.method == 'POST':
		form = CadastroServico(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/cadservico/')
		else:
			form = CadastroServico()

	context = {'form': CadastroServico()}	
	return render(request, 'cadastro_servico.html', context)


def submit_servico(request):

	servico_id = request.POST.get('servicoid')
	codigo = request.POST.get('codserv')
	servico = request.POST.get('desserv')
	tipo = request.POST.get('tipopet')
	tamanho = request.POST.get('tamanhopet')
	valor = request.POST.get('valor')
	ativo = request.POST.get('ativo')
	observacao = request.POST.get('observacao')


	if servico_id:
		servicos = Servico.objects.get(id=servico_id)
		servicos.codigo = codigo
		servicos.servico = servico
		servicos.tipo = tipo
		servicos.tamanho = tamanho
		servicos.valor = valor
		servicos.ativo = ativo
		servicos.observacao = observacao
		servicos.save()
		return redirect('/servicos/listservico')

	else:
		if servico == "" or tipo == "-------" or tamanho == "-------" or valor == "":
			erro = "Para salvar um serviço, verifique a descrição do serviço, o tipo, o tamanho e o valor."
			context = {'erro':erro}
			return render(request, 'cadastro_servico.html', context)
		else:
			servico_cad = Servico.objects.filter(servico=servico,tamanho=tamanho,tipo=tipo)

			if servico_cad:
				erro = "Já existe serviço cadastrado com esse nome, tipo e tamanho."
				context = {'erro':erro}
				return render(request, 'cadastro_servico.html', context)

		serviço = Servico.objects.create(codigo=codigo,servico=servico,tipo=tipo,tamanho=tamanho,valor=valor,ativo=ativo,observacao=observacao)

	return redirect('/servicos/cadservico/')