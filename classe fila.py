class fila():

    def __init__(self):
        self.data = []

    def inserir(self,x):
        self.data.append(x)

    def remover(self):
        if len(self.data) > 0:
            return self.data.pop(0)

    def proximo(self):
        if len(self.data) > 0:
            return self.data[0]

    def __repr__(self):
        return str(self.data)

def entrar():
    global filnor
    global filpri
    idade = int(input("Digite idade: "))
    if idade >= 60:
        filpri.inserir(idade)
    else:
        filnor.inserir(idade)

def sair():
   atendimento = 1
   global filnor
   global filpri
   if atendimento > 2:
       return filnor.remover()
       atendimento = 1
   else:
       return filpri.remover()
       atendimento = atendimento + 1

def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <=valor <=fim:
                return(valor)
        except ValueError:
            print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))

def exibe():
    global filnor
    global filpri
    print(filnor)
    print(filpri)
def menu():
    print("""
    0 - Encerra os trabalhos
    1 - Insere cliente na fila
    2 - Mostra fila
    3 - Finaliza atendimento
    """)
    return valida_faixa_inteiro("Escolha uma opção: ",0,2)


filnor = fila()
filpri = fila()

while True:
    opção = menu()
    if opção == 0:
        break
    elif opção == 1:
        entrar()
    elif opção == 2:
        exibe()
    elif opção == 3:
        sair()