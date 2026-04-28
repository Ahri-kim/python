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

#1338
L=['A', 'B', 'C', 'D','E','F','G','H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
n=int(input())
l=[[0]*t for t in range(1,n+1,1)]
J = 0
for i in range(n):
    K=0
    if i != 0:
        J = i
    for j in range(len(l[i])):
        if J > 25:
            J = J%26
        l[i][K]=L[J]
        J =J+n-j-1
        K +=1
for q in range(n):
    print(f"{' '.join(l[q]):>{n*2-1}}")

#3106
A = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
N , B = map(int,input().split())
l=[]
r=1
while N > 0:
    r=N%B
    N=N//B
    l.append(A[r])
print(''.join(l[::-1]))
'''
#1009
n = 1
while n!=0:
    n = input()
    s=0
    for i in range(len(n)):
        s+=int(n[i])
    print(n[::-1], s)