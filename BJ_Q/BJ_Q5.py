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
'''
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