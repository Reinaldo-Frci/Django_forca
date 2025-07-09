from django.shortcuts import render, redirect
from .models import Palavra, Partida
import random

def iniciar_jogo(request):
    palavra = random.choice(Palavra.objects.all())
    partida = Partida.objects.create(
        palavra=palavra,
        jogador="Anônimo"
    )
    request.session['partida_id'] = partida.id
    return redirect('jogo')

def jogo(request):
    partida_id = request.session.get('partida_id')
    if not partida_id:
        return redirect('iniciar_jogo')

    partida = Partida.objects.get(id=partida_id)
    palavra = partida.palavra.texto
    correto = palavra
    exibicao = ''

    for letra in palavra:
        if letra.lower() in partida.letras_certas:
            exibicao += f'{letra} '
        else:
            exibicao += '_ '

    if request.method == 'POST':
        letra = request.POST.get('letra').lower()
        if letra in palavra.lower():
            if letra not in partida.letras_certas:
                partida.letras_certas += letra
        else:
            if letra not in partida.letras_erradas:
                partida.letras_erradas += letra

        # Verificar vitória
        venceu = all(l.lower() in partida.letras_certas for l in palavra)
        partida.venceu = venceu
        partida.finalizada = venceu or len(partida.letras_erradas) >= 6
        partida.save()
        return redirect('jogo')

    contexto = {
        'correto': correto,
        'palavra': exibicao,
        'erros': partida.letras_erradas,
        'finalizada': partida.finalizada,
        'venceu': partida.venceu,
    }
    return render(request, 'jogo/jogo.html', contexto)

def reiniciar(request):
    request.session.flush()
    return redirect('iniciar_jogo')
