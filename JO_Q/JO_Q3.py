'''
#9698
N = int(input())
I1 = []
class XX:
    def __init__(self, Y, P):
        self.Y = Y
        self.P = P
for i in range(N):
    Y, P = map(int,input().split())
    I1.append(XX(Y, P))
A, B = map(int,input().split())
for t in I1:
    if t.Y >= A and t.P <= B:
        print(t.Y, t.P)

#9699
N, M = map(int,input().split())
L = []
class Xx:
    def __init__(self, n, s):
        self.n = n
        self.s = s
    def __str__(self):
        return f'{self.n}'
for i in range(N):
    n, s =input().split()
    if int(s) >= M:
        L.append(Xx(n, s))
    else:
        continue
for t in L[::-1]:
    print(t.n)

#9350
m = []
for i in range(5):
    m.append(int(input()))
print(*m)

#9351
m = []
for i in range(30):
    m.append(int(input()))
print(*m)

#9228
N = int(input())
if N >= 60:
    print('PASS')
else:
    print('FAIL')
'''
