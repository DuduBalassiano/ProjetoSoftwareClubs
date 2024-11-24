from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt  # Importa o decorador
from django.contrib.auth import authenticate, login
from django.contrib import messages

@csrf_exempt
def login_view(request):
    email = request.GET.get('email')
    password = request.GET.get('senha')

    if email and password:  # Se ambos os campos foram preenchidos
        user = authenticate(request, username=email, password=password)
        if user is not None:  # Se as credenciais forem válidas
            login(request, user)  # Faz login do usuário
            return redirect(f'/login/perfil/?email={email}&senha={password}')  # Redireciona com os dados
        else:
            messages.error(request, "Email ou senha inválidos.")  # Mensagem de erro

    return render(request, 'login.html')  # Recarrega a página de login

@csrf_exempt
def perfil_view(request):
    # Captura os parâmetros 'email' e 'senha' enviados via GET
    email = request.GET.get('email', 'Email não fornecido')  # Valor padrão se 'email' não for enviado
    senha = request.GET.get('senha', 'Senha não fornecida')  # Valor padrão se 'senha' não for enviado
    # Cria o contexto a ser enviado para o template
    context = {
        'email': email,
        'senha': senha,
    }
    # Renderiza o template 'perfil.html' com os dados do contexto
    return render(request, 'perfil.html', context)

@csrf_exempt
def cadastro_view(request):
    username = request.GET.get('username')
    email = request.GET.get('email')
    password = request.GET.get('password')

    if username and email and password:
        # Simula o cadastro
        messages.success(request, f"Usuário '{username}' cadastrado com sucesso!")
        return redirect('login')  # Redireciona para a página de login
    elif username or email or password:
        messages.error(request, "Todos os campos são obrigatórios!")

    return render(request, 'cadastro.html')