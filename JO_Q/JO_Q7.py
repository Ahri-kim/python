'''
#1314
n = int(input())
L=['A', 'B', 'C', 'D','E','F','G','H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
l = [[0]*n for _ in range(n)]
for i in range(1,n+1):
    if i ==1:
        for h in range(0,n,1):
            l[0][h] = L[h%26]
    elif i%2 != 0:
            J = 0
            for j in range(((i-1)*n),i*n,1):
                if j > 25:
                    j = j%26
                l[i-1][J] = L[j]
                J += 1
    else:
        K = 0
        for k in range(i*n-1,(i-1)*n-1, -1):  
            if k > 25:
                k = k%26
            l[i-1][K]=L[k]
            K += 1
for z in range(n):
    for x in range(n):
        print(l[x][z],end=' ')
    print()
'''
#1338
L=['A', 'B', 'C', 'D','E','F','G','H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
n=int(input())
l=[[0]*n for _ in range(n)]
M = 2*n-1
for i in range(0,n,1):
    if i > 25:
        i = i%26
        J = 0
    for j in range(n*(n+1)//2-1,0,-1):
        l[i][J]=L[j]
        J +=1
    print(l)