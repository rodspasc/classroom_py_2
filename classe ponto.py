class Point:
    "Classe cria pontos (x,y) int, int"

    def __init__(self, cordx = 0, cordy = 0):
        'inicializa coordenadas de um ponto'
        self.x = cordx
        self.y = cordy
 
    def setx(self,coordx):
        "define valor x Int"
        self.x = coordx

    def sety(self, coordy):
        "define valor y int" 
        self.y = coordy

    def get(self):
        "retorna ponto (x,Y)"
        return(self.x, self.y)

    def getx(self):
        return(self.x)

    def move(self, dx, dy):
        "move o ponto somando as coodernadas" 
        self.x += dx
        self.y += dy

    def __eq__(self, outro):
        'Retorna True se as cordenadas dos pontos forem iguais'
        return self.x == outro.x and self.y == outro.y

    def __repr__(self):
        'Retorna representação de string canonica Ponto(x,y)'
        return 'Ponto({},{})'.format(self.x, self.y)


class Vector(Point):

    def __add__(self, outro):
        'Soma objetos vetor'
        return self.x + outro.x, self.y + outro.y

    def __mul__(self, outro):
        'Retorna o produto das coodenadas de vetores'
        return self.x * outro.x + self.y * outro.y

    def __repr__(self):
        'Retorna representação string canônica'
        return 'Vetor{}'.format(self.get())
        
