# Transepose a matrix :

a = [[1,2,3],[4,5,6],[7,8,9]]

c = [[0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        c[i][j] = a[i][j]

for l in c:
    print(l)
