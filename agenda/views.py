from django.shortcuts import render, get_object_or_404, redirect
from .forms import CadastroTutor, CadastroPet, CadastroRaca
from .models import Tutor, Pet, Raca
from datetime import date



def calcula_idade(petidade):
	i = 0
	lid = []
	lidade = []
	lista = []
	while (i < len(petidade)):
		idt = petidade[i][0]
		dt_nas = petidade[i][1]
		hoje = date.today()
		idade = int(abs((hoje - dt_nas).days)//365.2524)
		lid.append(idt)
		lidade.append(idade)
		lista = list(zip(lid,lidade))
		i += 1
	return lista



def lista_raca(request):
	raca = Raca.objects.all().order_by('tipo', 'raca')
	context = {'raca': raca}
	return render(request, 'lista_raca.html', context)

def lista_pet(request):
	pet = Pet.objects.all()
	tutor = Tutor.objects.all()
	petidade = Pet.objects.values_list('id','dt_nascimento')
	idade = calcula_idade(petidade)
	context = {'pet':pet, 'tutor': tutor, 'idade': idade}
	return render(request, 'lista_pet.html', context)

def lista_tutor(request):
	tutor = Tutor.objects.all()
	pet = Pet.objects.all()
	context = {'tutor': tutor, 'pet':pet}
	return render(request, 'lista_tutor.html', context)


def cadastro_raca(request):
	raca_id = request.GET.get('id')

	if raca_id:
		altraca = Raca.objects.get(id=raca_id)
		return render(request, 'cadastro_raca.html', {'altraca': altraca})

	if request.method == 'POST':
		form = CadastroRaca(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/cadraca/')
		else:
			form = CadastroRaca()

	context = {'form': CadastroRaca()}

	return render(request, 'cadastro_raca.html', context)

def submit_raca(request):

	raca_id = request.POST.get('racaid')
	raca = request.POST.get('raca')
	tipo = request.POST.get('tipo')
	porte = request.POST.get('porte')


	if raca_id:
		racas = Raca.objects.get(id=raca_id)
		racas.raca = raca
		racas.tipo = tipo
		racas.porte = porte
		racas.save()
		return redirect('/agenda/listraca/')

	else:
		if raca == "" or tipo == "-------" or porte == "-------":
			erro = "Para salvar uma raça, verifique o nome da raça, o tipo e o porte."
			context = {'erro':erro}
			return render(request, 'cadastro_raca.html', context)
		else:
			raca_raca = Raca.objects.filter(raca=raca,tipo=tipo)

			if raca_raca:
				erro = "Já existe cadastrado uma raça com esse nome e tipo."
				context = {'erro':erro}
				return render(request, 'cadastro_raca.html', context)

		raca = Raca.objects.create(raca=raca,tipo=tipo,porte=porte)

	return redirect('/agenda/cadraca/')




def cadastro_tutor(request):
	tutor_id = request.GET.get('id')
	if tutor_id:
		alttutor = Tutor.objects.get(id=tutor_id)
		return render(request, 'cadastro_tutor.html', {'alttutor': alttutor})

	if request.method == 'POST':
		form = CadastroTutor(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/cadtutor/')
		else:
			form = CadastroTutor()

	context = {'form': CadastroTutor() }
	return render(request, 'cadastro_tutor.html', context)


def submit_tutor(request):

	tutor = request.POST.get('tutor')
	cpf = request.POST.get('cpf')
	tel_principal = request.POST.get('telprin')
	tel_alternativo = request.POST.get('telalt')
	email = request.POST.get('email')
	cont_alternativo = request.POST.get('contalt')
	tel_contato = request.POST.get('telcont')
	observacao = request.POST.get('observacao')
	tutor_id = request.POST.get('tutorid')

	if tutor_id:
		tutors = Tutor.objects.get(id=tutor_id)
		tutors.tutor = tutor
		tutors.cpf = cpf
		tutors.tel_principal = tel_principal
		tutors.tel_alternativo = tel_alternativo
		tutors.email = email
		tutors.cont_alternativo = cont_alternativo
		tutors.tel_contato = tel_contato
		tutors.observacao = observacao
		tutors.save()

		return redirect('/agenda/listtutor/')

	else:
		
		if tutor == "" or cpf == "" or tel_principal == "":
			erro = "Para salvar um tutor, verifique o nome do tutor, o seu cpf e o seu telefone principal."
			context = {'erro':erro}
			return render(request, 'cadastro_tutor.html', context)

		else:
			tutor_cpf = Tutor.objects.filter(cpf=cpf)
			if tutor_cpf:
				erro = "CPF já cadastrado em outro tutor."
				context = {'erro':erro}
				return render(request, 'cadastro_tutor.html', context)

		tutor = Tutor.objects.create(tutor=tutor,cpf=cpf,tel_principal=tel_principal,tel_alternativo=tel_alternativo,
		email=email,cont_alternativo=cont_alternativo,tel_contato=tel_contato,observacao=observacao)
		
	return redirect('/agenda/cadpet/')


def cadastro_pet(request):
	tutor = Tutor.objects.all().order_by('tutor')
	racas = Raca.objects.all().order_by('tipo', 'raca')
	pet_id = request.GET.get('id')
	if pet_id:
		altpet = Pet.objects.get(id=pet_id)
		return render(request, 'cadastro_pet.html', {'altpet': altpet, 'tutor': tutor, 'racas': racas})

	if request.method == 'POST':
		form = CadastroPet(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/cadpet/')
		else:
			form = CadastroPet()

	context = {'form': CadastroPet(), 'tutor': tutor, 'racas': racas  }

	return render(request, 'cadastro_pet.html', context)



def submit_pet(request):

	pet_id = request.POST.get('petid')
	pet = request.POST.get('nomepet')
	tipo = request.POST.get('tipopet')
	raca = request.POST.get('racapet')
	tamanho = request.POST.get('tamanhopet')
	cor = request.POST.get('corpet')
	dt_nascimento = request.POST.get('dtnascimento')
	tutor = request.POST.get('tutor')
	pet_alergico = request.POST.get('petalerg')
	pet_cardiaco = request.POST.get('petcard')
	observacao = request.POST.get('observacao')

	if pet_id:
		pets = Pet.objects.get(id=pet_id)
		pets.pet = pet
		pets.tipo = tipo
		pets.raca = raca
		pets.tamanho = tamanho
		pets.cor = cor
		pets.dt_nascimento = dt_nascimento
		pets.tutor = tutor
		pets.pet_alergico = pet_alergico
		pets.pet_cardiaco = pet_cardiaco
		pets.observacao = observacao
		pets.save()
		return redirect('/agenda/listpet/')

	else:

		if pet == "" or tipo == "-------" or raca == "-------" or tamanho == "-------" or tutor == "-------":
			erro = "Para salvar um pet, verifique o nome do pet, o seu tipo, a sua raça, o seu tamanho e o tutor atrelado a ele."
			context = {'erro':erro}
			return render(request, 'cadastro_pet.html', context)

		else:
			pet_tutor = Pet.objects.filter(tutor=tutor)

			if pet_tutor:
				erro = "Já existe cadastrado um pet com esse tutor."
				context = {'erro':erro}
				return render(request, 'cadastro_pet.html', context)

		pet = Pet.objects.create(pet=pet,tipo=tipo,raca=raca,tamanho=tamanho,cor=cor,dt_nascimento=dt_nascimento,
		tutor=tutor,pet_alergico=pet_alergico,pet_cardiaco=pet_cardiaco,observacao=observacao)

	return redirect('/agenda/cadpet/')



