palavras = []
x=0
while x==0:
    palavras.append(input("Digite uma palavra "))
    fim = input("Deseja digitar outra palavra (n)Não? ")

    if fim == "n":
        print(fim)
        x=1

print(palavras)

for c in palavras:
    if len(c) == 4:
        print(c)

