class Criatura:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricap = descricao
        self.pontos_vida = 50
        self.habilidades = {'Combate corpo a corpo',
                            'Atira flechas enquanto corre', 'Grande velocidade'}
        self.dano_base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def golpear_criatura(self, valor_golpe):
        self.pontos_vida -= valor_golpe
        print(f"O {self.nome} recebeu o dano de {valor_golpe} e sua vida atual é de {self.pontos_vida}")

    def __str__(self):
        return f'DADOS DA CRIATURA:\n Nome: {self.nome}\n Pontos de Vida: {self.pontos_vida}'


class Personagem:
    def __init__(self, vocacao, nome, pontos_vida):
        self.vocacao = vocacao
        self.nome = nome
        self.nivel = 1
        self.pontos_vida = pontos_vida
        self.dano_base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def golpear_jogador(self, valor_golpe):
        self.pontos_vida -= valor_golpe
        print (f"O {self.nome} recebeu o dano de {valor_golpe} e sua vida atual é de {self.pontos_vida}")
    
    def __str__(self):
        return f"DADOS DO PERSONAGEM:\n Nome: {self.nome}\n Pontos de Vida: {self.pontos_vida}\n Nível: {self.nivel}\n Vocação: {self.vocacao}"