'''
#25304
X=int(input())
A=[]
B=[]
total = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    
for t in range(len(A)):
    total += A[t] * B[t]

if X==total:
    print('yes')
else:
    print('no')

#25314
N = int(input())
M = N//4
def f(M):
    return 'long '*M
result=f(M).strip()
print(result,'int')

#15552
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)

#11021
import sys

T = int(sys.stdin.readline())
X=[]
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    X.append(A+B)
for t in range(len(X)):
    print(f'Case #{(t+1)}:',X[t])

#11022
import sys
a = []
b = []
T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    a.append(A)
    b.append(B)

for n in range(len(a)):
    print(f'Case #{n+1}:', a[n],'+', b[n],'=', a[n] + b[n] )

#10871
N, X = map(int,input().split())
for n in map(int, input().split()):
    if n < X:
        print(n,end = ' ')

#2438
N = int(input()) 
for i in range(N): 
    print('*'*(i+1))

#2439
N = int(input())
for i in range(N):
    print(('*'*(i+1)).rjust(N))

#10952
A = []
while True:
    a, b = map(int,input().split())
    if a==0 and b==0:
        break
    else:
        A.append(a+b)
for i in A:
    print(i)
'''
#10951
