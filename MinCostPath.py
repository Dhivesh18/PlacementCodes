'''
a = [[2,3,4]
     [5,9,8]
     [7,2,1]]
m,n = 2,2
minimumCostPath = [[2, 5, 9  ] 
                   [7, 11, 13]
                   [14, 9, 10]]
'''
def minCostpath(a,m,n):
    minc=[[0 for _ in range(n+1)] for _ in range(m+1)]
    minc[0][0] = a[0][0]
    for i in range(1,m+1):
        minc[i][0]=minc[i-1][0]+a[i][0]
    for j in range(1,n+1):
        minc[0][j]=minc[0][j-1]+a[0][j]
    for i in range(1,m+1):
        for j in range(1,n+1):
            l,ab,d=minc[i-1][j],minc[i][j-1],minc[i-1][j-1]
            minc[i][j]=a[i][j]+min(l,ab,d)
    return minc[m][n]

a,m,n=[[2,3,4],[5,9,8],[7,2,1]],2,2
print(minCostpath(a,m,n))
