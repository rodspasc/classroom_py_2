class retangulo:
    'define retangulos'
    def setTamanho(self, comprimento, largura):
        'define comprimento e largura do retangulo'
        self.comp = comprimento
        self.larg = largura
    def perimetro(self):
        'reorna o perimetro do retangulo'
        return self.comp*2 + self.larg*2
    def area(self):
        'retorna a area do retangulo'
        return self.comp * self.larg
        
