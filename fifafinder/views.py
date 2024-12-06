from django.contrib import messages
from .forms import PlayerForm
from django.shortcuts import render

def add_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o jogador no banco de dados
            return redirect('home')  # Redireciona para a página inicial (ou qualquer outra página)
    else:
        form = PlayerForm()  # Se o método for GET, apenas exibe o formulário

    return render(request, 'add_player.html', {'form': form})


# Função que renderiza a página inicial
def home_view(request):
    return render(request, 'home.html')