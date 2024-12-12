from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import PlayerForm
from .forms import ChampionshipForm

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email and password:
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                return redirect('perfil')
            else:
                messages.error(request, "Email ou senha inválidos.")
    return render(request, 'login.html')


@csrf_exempt
def perfil_view(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')

    context = {'user': user}
    return render(request, 'perfil.html', context)


@csrf_exempt
def cadastro_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if username and email and password:
            # Aqui você poderia criar um novo usuário
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('login')
        else:
            messages.error(request, "Todos os campos são obrigatórios.")
    return render(request, 'cadastro.html')


def home(request):
    return render(request, 'home.html')

   

def add_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o jogador no banco de dados
            return redirect('home')  # Redireciona para a página inicial (ou qualquer outra página)
    else:
        form = PlayerForm()  # Se o método for GET, apenas exibe o formulário

    return render(request, 'add_player.html', {'form': form})

'''def add_championship(request):
    if request.method == 'POST':
        form = ChampionshipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Substitua 'home' pela URL da página inicial ou lista de campeonatos
    else:
        form = ChampionshipForm()
    return render(request, 'add_championship.html', {'form': form})'''

def add_championship(request):
    return render(request, 'add_championship.html')