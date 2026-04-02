'''
#2675
T = int(input())
E = []
for _ in range(T):
    R, S = input().split()
    r = ""
    for i in S:
        r += i * int(R)
    E.append(r)
print('\n'.join(E))

#1152
S = input().split()
print(len(S))

#2908
A, B = input().split()
a = int(A[::-1])
b = int(B[::-1])
if a > b:
    print(a)
else:
    print(b)

#2558
A = int(input())
B = int(input())
print(A + B)

#10951
import sys
for i in sys.stdin:
    A, B = map(int,i.split())
    print(A+B)

#10953
import sys
T = int(sys.stdin.readline())
S = []
for _ in range(T):
    i = sys.stdin.readline()
    A, B = i.split(',')
    S.append(int(A) + int(B))
for t in S:
    print(t)

#15740
import sys
A ,B = map(int,sys.stdin.readline().split())
print(A / B)

#5622
d = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I'],
    ['J', 'K', 'L'],
    ['M', 'N', 'O'],
    ['P', 'Q', 'R', 'S'],
    ['T', 'U', 'V'],
    ['W', 'X', 'Y', 'Z']
]
w = input()
A = []
for a in w:
    found = False
    for i in range(len(d)):
        for j in range(len(d[i])):
            if d[i][j] == a:
                b = i
                c = b + 2
                A.append(c)
                found = True
                break  
        if found:
            break
print(sum(A) + len(A))

#11718
import sys

while True:
    I = sys.stdin.readline().strip()
    print(I)

    if not I:
        break


#25083
#print(r''
#         ,r'"7
#r`-_   ,'  ,/
# \. ". L_r'
#   `~\/
#      |
#      |'')

#3003
import sys
C = list(map(int,sys.stdin.readline().strip().split()))
c = [1, 1, 2, 2, 2, 8]
r = []
for i in range(6):
    r.append(c[i] - C[i])
print(*r)

#2444
N = int(input())
M = 2*N-1
for i in range(1,M+1,2):
    S = (M-i)//2
    print(' '*S + '*'*i)
for j in range(M-2,0,-2):
    S = (M - j)//2
    print(' ' * S +'*'*j)

#1546
import sys
s = 0
N = int(sys.stdin.readline().strip())
a = list(map(int,sys.stdin.readline().strip().split()))
for i in a:
    s += ((i / max(a)) * 100)
print(s/N)

#10811
import sys
N, M = map(int,sys.stdin.readline().strip().split())
L = []
for t in range(N):
    L.append(t+1)
for _ in range(M):
    i, j = map(int,sys.stdin.readline().split())
    p = L[i-1:j]
    p = p[::-1]
    L[i-1:j] = p
print(*L)
'''
#1149
import sys 
N = int(sys.stdin.readline().strip()) 
L = [0, 0, 0] 
m = 0 
F = 0 
for t in range(N): 
    r, g, b = map(int,sys.stdin.readline().split()) 
    L[0], L[1], L[2] = r, g, b 
    if t == 0: 
        F += L.index(min(L)) 
        m += min(L) 
    else:
        if F == 0: 
            m += min(L[1:3])
            F = L.index(min(L[1:3]))
        elif F == 1: 
            s = min(L[0], L[2]) 
            m += s 
            F = L.index(min(L[0], L[2]))
        else:
            m += min(L[:1]) 
            F = L.index(min(L[:1]))
print(m)