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

#--------------------------------------------------------------------------------

#9324
i=1
while i<=3:
    print('*'*i)
    i+=1

for i in range(1,4,1):
    print('*'*i)

#9325
t=1
n=int(input())
while t<=n:
    print('*'*t)
    t+=1

n=int(input())
for t in range(1,n+1):
    print('*'*t)

#9327
for i in range(3,1,-1):
    print('*'*i)
for i in range(1,4,1):
    print('*'*i)

#9328
n=int(input())
t=1
while t<=n:
    print('*'*t)
    t+=1
while t!=1:
    t-=1
    print('*'*t)

#9326
n=int(input())
for i in range(n,0,-1):
    print('* '*i)

#9329
for i in range(1,4,1):
    print(f"{'*'*i:>3}")

#9330
n=int(input())
for i in range(n,0,-1):
    print(f"{'*'*i:>{n}}")

#9331
for i in range(1,6,2):
    print(f"{'*'*i:^5}")

#1304
n = int(input())
for j in range(n):
    for i in range(j+1, n*n+1, n):
        print(i, end = ' ')
    print()

#1146
n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)-1):
    m=l[i:].index(min(l[i:]))+i
    l[m],l[i] = l[i],l[m]
    print(*l)

#9466
n=int(input())
def f():
    for i in range(1,n*n+1,1):
        if i%n!=0:
            print(i,end=' ')
        else:
            print(i)
            print()
f()

#2604
n=list(input())
s=0
for i in range(len(n)-1):
    if n[i] == n[i+1]:
        s+=5
    else:
        s+=10
print(s+10)

#2857
l = [list(input()) for _ in range(5)]
m = len(max(l, key=len))
for j in range(m):
    for i in range(5):
        if len(l[i]) > j:
            print(l[i][j], end='')
'''
#2071
n,m=map(int,input().split())
l = [[1]*t for t in range(1,n+1)]
print(l)
#if m==1:
#    for i in range(n):
        
#    print()
#elif m==2:
#else:
