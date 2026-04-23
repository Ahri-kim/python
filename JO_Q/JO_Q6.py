'''
#9312
for j in range(1, 10):
    for i in range(5, 8):
        print(f"{i} * {j} = {i*j}",end='   ')
    print()

#9323
s = int(input())
e = int(input())
for i in range(1, 10):
    if s < e:
        for j in range(s, e+1):
            print(j,'*',i,'=',i*j, end = '   ')
        print()
    else:
        for j in range(s, e-1, -1):
            print(j,'*',i,'=',i*j, end = '   ')
        print()

#9404
S = input().split()
I = list(map(int,input().split()))
F = list(map(float,input().split()))
print(S)
print(I)
print(F)

#9405
N = list(map(int,input().split()))
print(N)
print(*N)
print('hap =',sum(N))

#9406
t = 1
C = [0,0,0,0,0,0,0,0,0,0,0]
L = []
while t != 0:
    t = int(input())
    if t <= 0 or t > 11:
        break
    elif t in L:
        C[t] += 1
    else:
        L.append(t)
        C[t] += 1
L.sort()
for i in L:
    print(f"{i}: {C[i]}")

#9407
L = list(map(int,input().split()))

#9369
l = []
t = 0
while t != -1:
    t = int(input())
    l.append(t)
    if t != -1:
        if len(l) > 3:
            l.pop(0)
    else:
        l.pop()
print(*l)

#9390
h = int(input())
m = int(input())
if h < 10:
    if m < 10:
        print(f"0{h}:0{m}")
    else:
        print(f"0{h}:{m}")
elif h>10 and m < 10:
    print(f"{h}:0{m}")
else:
    print(f"{h}:{m}")

#9462
n = int(input())
i = list(map(int,input().split()))
l = len(i)
for k in range(l-1):
    swapped = False
    for j in range(0, l - k - 1):
        if i[j] > i[j + 1]:
            i[j], i[j + 1] = i[j + 1], i[j]
            swapped = True
    print(i)

#1291
s, e = map(int,input().split())
while s<2 or s>9 or e<2 or e>9:
    print("INPUT ERROR!")
    s, e = map(int,input().split())
if s < e :
    for j in range(1, 10):
        for i in range(s, e+1):
            print(f"{i} * {j} = {i*j:2d}",end='   ')
        print()
else:
    for j in range(1, 10):
        for i in range(s,e-1,-1):
            print(f"{i} * {j} = {i*j:2d}",end='   ')
        print()

#1341
s, f = map(int,input().split())
if s < f:
    for j in range(s, f+1,1):
        for i in range(1, 4, 1):
            print(f"{j} * {i} = {i*j:2d}",end='   ')
        print()
        for i in range(4, 7, 1):
            print(f"{j} * {i} = {i*j:2d}",end='   ')
        print()
        for i in range(7, 10, 1):
            print(f"{j} * {i} = {i*j:2d}",end='   ')
        print()
        print()
else:
    for j in range(s, f-1, -1):
        for i in range(1, 4, 1):
            print(f"{j} * {i} = {i*j:2d}",end='   ')
        print()
        for i in range(4, 7, 1):
            print(f"{j} * {i} = {i*j:2d}",end='   ')
        print()
        for i in range(7, 10, 1):
            print(f"{j} * {i} = {i*j:2d}",end='   ')
        print()
        print()

#1303
n, m = map(int,input().split())
a = n*m
for i in range(1,n+1,1):
    if i == 1:
        for k in range(1,m+1,1):
            print(k,end=' ')
        print()
    else:
        for j in range((i-1)*m+1,i*m+1,1):
            print(j,end=' ')
        print()

#9702
class P:
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age
l=[]
n = int(input())
for i in range(n):
    Name, Age = input().split()
    l.append(P(Name, Age))
L = sorted(l, key=lambda x: x.Age, reverse=True)
for p in L:
    print(f"Name:{p.Name}, Age:{p.Age}")

#1856
n, m = map(int,input().split())
for i in range(1, n+1,1):
    if i==1:
        for t in range(i,m+1,1):
            print(t,end=' ')
        print()
    elif i%2!=0:
        for j in range(((i-1)*m)+1,(i*m)+1,1):
            print(j,end=' ')
        print()
    else:
        for k in range(i*m,(i-1)*m,-1):
            print(k,end=' ')
        print()

#1304
n = int(input())
for j in range(n):
    for i in range(j+1, n*n+1, n):
        print(i, end = ' ')
    print()

#5931
n = int(input())
for i in range(1,n+1,1):
    for t in range(n):
        print(i,end=' ')
    print()

#5932
n = int(input())
l = list(range(1, n+1))

for i in range(n):
    print(*l if i % 2 == 0 else l[::-1])

#5933
n = int(input())
for i in range(1,n+1):
    for j in range(i,(i*n)+1,i):
        print(j,end=' ')
    print()

#1307
L=['A', 'B', 'C', 'D','E','F','G','H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
n = int(input())
for i in range(1,n+1):
    for j in range((n*n)-i, -1, -n):
        j = j%26            
        print(L[j],end=' ')
    print()

#9391
h ,m = map(int,input().split())
if h>=12:
    if h !=12:
        print(f"{h-12:02} : {m} PM")
    else:
        print(f"{h} : {m} PM")
else:
    print(f"{h:02} : {m} AM")
'''