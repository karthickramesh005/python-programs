# Add the two matrix :

a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[11,21,34],[44,54,63],[73,82,29]]
c = [[0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        c[i][j] = a[i][j]+b[i][j]

print(c)
