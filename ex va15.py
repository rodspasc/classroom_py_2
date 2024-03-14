n1 = float(input('Digite a nota N1 '))
n2 = float(input('Digite a nota N2 '))
media = 0.4*n1 + 0.6*n2
if media >= 5.0:
    print('Você está aprovado e sua nota final é', media, 'Parabens!!!')
else:
    print('Você está reprovado sua nota final é', media, 'Estude mais')
