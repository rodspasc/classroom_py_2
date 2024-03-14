class Animal:
    'representa um animal'
    
    def __init__(self, espécie, linguagem):
        'inicializa o animas e suas caracteristicas'
        self.esp = espécie
        self.ling = linguagem


    def fala(self):
        'exibe uma sentença para o animal'
        print("Eu sou um {} e sei falar {}".format(self.esp, self.ling))
        
              
