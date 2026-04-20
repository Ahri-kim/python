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
'''
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