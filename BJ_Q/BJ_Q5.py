'''
#1157
from collections import Counter
import sys
W = list(sys.stdin.readline().strip())
if len(W) == 1:
    w = W[0]
    print(w.upper())
else:
    U = ''.join(W)
    W = U.upper()
    C = Counter(W)
    L = list(C.items())
    L.sort(key=lambda x: x[1], reverse=True)
    if len(L) > 1 and L[0][1] == L[1][1]:
        print('?')
    else:
        print(L[0][0])

#2941
import sys
A = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = 0
W = sys.stdin.readline().strip()
for cro in A:
    if cro in W:
        count = W.count(cro)
        s += count
        W = W.replace(cro, '0')
for i in W:
    if i.isalpha():
        s += 1
print(s)

#1316
import sys
W = ''
S = []
s = 0
N = int(sys.stdin.readline().strip())
for i in range(N):
    w = sys.stdin.readline().strip()
    S.append(w)
    for j in range(len(w)):
        if j != len(w):
            if S[j] == S[j + 1]:
                S.add(j)
                s += 1
            elif S[j] == S[j-1]:
                S.add(j)
                s += 1
            elif j in S:
                s -= 1
            else:
                s +=1
        elif S[j] == S[j-1]:
            S.add(j)
            s += 1
        elif j in S:
            s -= 1
        else:
            s +=1
print(s)

#2292
N = int(input())
s = 1
a = 1 
while N > a:
    a += 6 * s
    s += 1
print(s)

---------------------------------------------------------------------
N = int(input())
M = N//6 
A = []
s = [1]
if N == 1:
    print(1)
elif 1 < N <= 7:
    print(2)
elif N != 1:
    for i in range(1,M + 2):
        A.append(6*i)
        if i == 1:
            s.append(7)
        else:
            s.append(A[i-1]+s[i-1])
for j in range(1, len(s)):
    if s[j]< N <= s[j+1]:
        print(j+2)
---------------------------------------------------------------------        

#2745
A = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N',
'O','P','Q','R','S','T','U','V','W','X','Y','Z']

N , B = input().split()
b = int(B)
n = len(N)
s = 0
for i in N:
    I = A.index(i)
    s += I*(b**(n-1))
    n -= 1
print(s)

#2869
a, b, v = map(int,input().split())
d = a-b
w = v - a

if a==v:
    print(1)
elif d != 1:
    if w%d==0:
        print((w//d)+1)
    else:
        print((w//d)+2)
else:
    print(w +1)

#25206
grade = {
"A+":4.5, "A0":4.0,
"B+":3.5, "B0":3.0,
"C+":2.5, "C0":2.0,
"D+":1.5, "D0":1.0,
"F":0.0
}
T = 0
A = 0
for _ in range(20):
    s, h, g = input().split()
    h = float(h)
    if g == "P":
        continue
    T += h
    A += h * grade[g]
print(A / T)

#3046
r1, s = map(int,input().split())
print((s*2)-r1)
'''
#2638
n, m = map(int,input().split())
L =[]
l = []
T = 0
for i in range(n):
    L.append(input().split())
for i in range(len(L)):
    for j in range(len(L[0])):
        if L[i][j] == '1':
            l.append((i,j))

if L[i-1][j] == '0' or L[i+1][j] == '0':
    if L[i][j-1] == '0' or L[i][j+1] == '0':
        T += 1





for k in range(len(l)):