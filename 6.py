import classes as cl
import random

def criar_jogador():
    x = input("Qual classe você deseja?\nPaladino, Sorcerer, Druid ou Knight\n: ")
    pontos_vida = 0
    nome = input("qual o seu nome?\n: ")
    if x == 'Paladino':
        pontos_vida = 40
    elif x == 'Sorcerer':
        pontos_vida = 30
    elif x == 'Druid':
        pontos_vida = 20
    elif x == 'Knight':
        pontos_vida = 50
    return cl.Personagem(x,nome,pontos_vida)

orc = cl.Criatura("Orcão", "É verde e taca pedra")
player = criar_jogador()
rodada = 0
print (f'Bem vindo, {player.nome}! a batalha logo irá começar!')

while (rodada != 6):
    orc.golpear_criatura(random.choice(player.dano_base))
    player.golpear_jogador(random.choice(orc.dano_base))
    rodada += 1