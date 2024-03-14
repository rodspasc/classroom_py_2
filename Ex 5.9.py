def soma2d(t,s):
    for i in range(len(t)):
        for j in range(len(t[0])):
            s[i][j] = s[i][j] + t[i][j]
    return(s)

t = [[4,7,2,5],[5,1,9,2],[8,3,6,6]]

s = [[0,1,2,0],[0,1,1,1],[0,1,0,0]]

soma2d(t,s)
print(s)
