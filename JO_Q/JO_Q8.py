'''
n, m = map(int,input().split())
l = [[0]*m for _ in range(n)]
for i in range(n):
    l[i] = list(map(int, input().split()))
L = [row[:] for row in l]
c = sum(row.count(1) for row in l)
C=1
T=0
i=0
while C != 0:
    for row in l:
        if 1 in row:
            for j in range(1,m):
                if row[j] == 1:
                    if l[i-1][j]+l[i][j-1]+l[i+1][j]+l[i][j+1]<3:
                        L[i][j]=0
            i+=1
        else:
            i+=1
    i=0    
    l=[row[:] for row in L]
    C=sum(row.count(1) for row in l)
    if c != C:
        T += 1
        c = C    
print(T)
'''
#--------------------------------------------------------------------------------
