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
A = {'a':10,'b':11,'c':12,'d':13,'e':14,'f':15,'g':16,'h':17,'i':18,'j':19,'k':20,'l':21,'m':22,'n':23,
'o':24,'p':25,'q':26,'r':27,'s':28,'t':29,'u':30,'v':31,'w':32,'x':33,'y':34,'z':35}
#print(A['a'])



R = 0
for x in N:
    if 0 <= N <= 9:
        R = R * B + int(x)
    else:
        R = R * B + int(A['x'])

print(R)
'''

N , B = input().split()
b = int(B)
r = int("N", b)
print(r)
l = int("1z", 36)
print(l)