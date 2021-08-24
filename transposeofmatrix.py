import numpy

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

#1 4 7
#2 5 8
#3 6 9

res=[ [0 for i in range(3) ]for j in range(3)]
#print(res)
for i in range(3):
    for j in range(i+1,3):
        mat[i][j],mat[j][i]=mat[j][i] , mat[i][j]


#print(mat)
print(numpy.rot90(mat,k=4,))


