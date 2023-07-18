from ast import literal_eval
n =int(input()) #number of cities
from sys import  maxsize
from itertools import  permutations
V=n
def travellingSalesmanProblem(graph, s):
    resultper=0
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation = permutations(vertex)
    resultper=next_permutation
    for i in next_permutation:

        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
        if current_pathweight < min_path:
            resultper =  next_permutation

        # update minimum
        min_path = min(min_path, current_pathweight)



    return min_path
    #return resultper


#coordinates=[]
#strs = input()
#coordinates.append(literal_eval(strs.replace(' ',',')))
#print(coordinates)
dist_matrix = []
for i in range(n):
    rows = list(map(float,input().split()))
    dist_matrix.append(rows)
print(dist_matrix)

print(travellingSalesmanProblem(dist_matrix,0))
# for k in travellingSalesmanProblem(dist_matrix,0):
#     print(k)