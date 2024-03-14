class Queue:
    'uma classe de fila classica'

    def __init__(self):
        'instancia uma lista vazia'
        self.q = []

    def isEmpty(self):
        'retorna True se a fila estiver vazia'
        return(len(self.q) == 0)

    def enqueue(self, item):
        'insere item no final da fila'
        return self.q.append(item)

    def dequeue(self):
        'remove e retorna item na frente da fila'
        return self.p.pop(0)

    def __eq__(self, outro):
        ' retorna True se as filas self e outro tiverem os mesmos itens na mesma ordem'
        return self.q == outro.q

    def __len__(self):
        'retorna número de itens na fila'
        return len(self.q)

    def __repr__(self):
        'retorna representação de string canonica da fila'
        return 'Queue({})'.format(self.q)
