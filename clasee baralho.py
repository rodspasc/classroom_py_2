from random import shuffle

class Baralho:
    'Representa um baralho de 52 cartas'
    # valores e naipes são variaveis da classe Baralho
    valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    naipes = ['\u2662','\u2661','\u2662','\u2663']

    def __init__(self):
        'inicializa um baralho com 52 cartas'
        self.baralho = []
        for naipe in Baralho.naipes:
            for valor in Baralho.valores:
                self.baralho.append((valor, naipe))
                
    def embaralha(self):
        'embaralha as cartas'
        shuffle(self.baralho)

    def distribuiCarta(self):
        'distribui (remove e retorna) carto do topo do baralho'
        return self.baralho.pop()

    def __repr__(self):
        return str(self.baralho)
        

    
