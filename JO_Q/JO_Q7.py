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

#1534
A = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
N , B = map(int,input().split())
l=[]
r=1
while N > 0:
    r=N%B
    N=N//B
    l.append(A[r])
print(''.join(l[::-1]))

#1009
n = 1
while True:
    n = input().strip()
    if n == '0':
        break
    s=0
    for i in range(len(n)):
        s+=int(n[i])
    print(int(n[::-1]), s)

#9463
i = list(map(int,input().split()))
l = len(i)
for k in range(l-1):
    swapped = False
    for j in range(0, l - k - 1):
        if i[j] < i[j + 1]:
            i[j], i[j + 1] = i[j + 1], i[j]
            swapped = True
    print(*i)

#1692
a=int(input())
b=input()
print(a * int(b[2]))
print(a * int(b[1]))
print(a * int(b[0]))
print(a * int(b))

#1430
a=int(input())
b=int(input())
c=int(input())
d=str(a*b*c)
for i in range(10):
    print(d.count(str(i)))

#1071
n=int(input())
l=list(map(int,input().split()))
m=int(input())
s=0
u=0
for i in l:
    if m%i==0:
        if i in l:
            s+=i
    if i%m==0:
        if i in l:
            u+=i
print(s)
print(u)
'''
#1733
n = []
for i in range(19):
    n.append(list(map(int, input().split())))
s=[]
J=[]
K=[]
T=0
while T==0:
    for j in range(19):
        for k in range(19):
            if n[j][k] !=0:
                for x in range(1,6):
                    if j+x <= 18 and k+x <= 18:
                        if n[j][k+x] == n[j][k] or n[j+x][k] == n[j][k] or n[j+x][k+x] == n[j][k]:
                            s.append(n[j][k])
                            J.append(j)
                            K.append(k)
                        else:
                            break
                if 0<=len(s)<=4:
                    s=[]
                    J=[]
                    K=[]
                else:
                    T=1
        if j ==18 and len(s)==0:
            s.append(0)

print(s)
print(J)
print(K)
'''
if s[0] != 0:
    print(s[0])
    print(J[0], K[0])
else:
    print(0)
'''






#    n[j][k+1]==n[j][k] or n[j+1][k+1]==n[j][k] or n[j+1][k]==n[j][k]