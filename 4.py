import classes

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
    
    return classes.Personagem(x,nome,pontos_vida)

jogador = criar_jogador()
print(jogador)