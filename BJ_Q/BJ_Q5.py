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
'''
#2292
N = int(input())
M = N//6
A = [0,0]
if N == 1:
    print(1)
elif 1 < N <= 7:
    print(2)
else:
    for i in range(M-1,M+2):
        A[i] = (1+3*(i*(i+1)))
        for j in range(2,len(A)+5):
            if j != A[len(A)] and j< N <= A[j+1]:
                print(j+2)
    
    '''
    print(M+1)
    1+3(n*(n+1))

#A = []
#s = []
else:
    

for j in range(len(A)):        
    
        

        else:
            s.append(A[i-1]+s[i-1])
for j in range(1, len(s)):
    if s[j]< N <= s[j+1]:
        print(j+2)

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
'''

#               1+6(1+2)-7                  1+6(1+2+3+4)-
#           1+6*1   (1+6*1)+(6*2)   {(1+6*1)+(6*2)}+(6*3)   
#           1+6(1)  1+6(1+2)        1+6(1+2+3)      1+6(1+2+3+4)        1+3(n*(n+1))
# s  1   -   7   -   19      -       37      -       61      -       91    -     127
# A      6   -   12    -    18      -       24       -       30      -     36
# A    6*1      6*2       6*3             6*4               6*5           6*6
#   