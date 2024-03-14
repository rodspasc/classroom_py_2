def meuIMC(altura,peso):
    imc = peso/altura**2
    if imc < 18.5:
        print('Abaixo do peso')
    elif imc >= 18.5 and imc < 25:
        print('Normal')
    else:
        print('Sobrepeso')

peso = float(input('Digite seu peso em quilogramas '))
altura = float(input('Digite sua altura em metros '))
meuIMC(altura,peso)