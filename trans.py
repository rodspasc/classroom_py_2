
def transp(m):
    t = []
    if len(m) == len(m[0]):
        for y in range(len(m)):
            linha = []
            for x in range(len(m[0])):
                linha.append(0)
            t.append(linha)

        for i in range(len(m)):
            for j in range(len(m[0])):
                t[i][j] = m[j][i]
    else:
        for y in range(len(m[0])):
            linha = []
            for x in range(len(m)):
                linha.append(0)
            t.append(linha)

        for i in range(len(m[0])):
            for j in range(len(m)):
                t[i][j] = m[j][i]
    return(t)

