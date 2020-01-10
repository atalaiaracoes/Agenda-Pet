from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required



@login_required(login_url='/')
def index(request):
	return render(request, 'inicial.html')

def glogin(request):
	return render(request, 'login.html')

def glogout(request):
	logout(request)
	return redirect('/')

@csrf_protect
def submit(request):
	username = request.POST.get('username')
	password = request.POST.get('password')

	user = authenticate(username=username, password=password)

	if user is not None:
		if user.is_active:
			login(request,user)
			return redirect('index')
	else:
		erro = "Usuário e/ou senha não cadastrados."
		context = {'erro': erro}
		return render(request, 'login.html', context)

	return redirect('')
