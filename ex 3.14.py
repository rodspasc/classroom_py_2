def trocaPU(lst):
    lst[0],lst[len(lst)-1] = lst[len(lst)-1], lst[0]
    print(lst)

trocaPU( ['farinha', 'açúcar', 'manteiga', 'maçãs','mamão'])
