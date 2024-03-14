def average(x,y):
    'calcula a média entre dois valores x e y => float or int '
    aver = (x+y)/2
    print(aver)


def negativos(lst):
    'exibe os números negativos contidos em uma lista'
    for i in lst:
        if i < 0:
            print(i)


help(average)
help(negativos)