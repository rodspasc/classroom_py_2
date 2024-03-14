class Queue2(list):
    'uma classe fila, subclasse list'

    def isEmpty(self):
        'retorna True se fila vazia'
        return (len(self) == 0)

    def dequeue(self):
        'remove e retorna item na frente da fila'
        return self.pop(0)

    def enqueue(self, item):
        'insere item no final da fila'
        return self.append(item)
    
