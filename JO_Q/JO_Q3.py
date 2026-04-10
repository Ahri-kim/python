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

#9385
N, A = input().split()
n, a = input().split()
print(f"{N}'s age - {n}'s age =", int(A)-int(a))

#9229
A = int(input())
if A >=13:
    print("Middle School")
else:
    print("Elementary School")

#9352
L =[]
for i in range(50):
    L.append(int(input()))
print(*L[::-1])

#9290
N = int(input())
for i in range(N):
    print('Python',i)

#9294
N = int(input())
for i in range(1,N+1,1):
    print(i, end =' ')

#9382
A = "apple orange banana"
B = "   Hello world!   "
A = "banana orange apple"
print(A)
print(B)
print(B.strip())

#9353
A = ['a','b','c','d','e']
print(A)
print(*A[::-1])

#9458
N = int(input())
def f():
    if N>0:
        print('positive')
    elif N == 0:
        print('zero')
    else:
        print('negative')
f()

#9459
G, A = input().split()
if G =='m' or G == 'M':
    if int(A) >=20:
        print('MAN')
    else:
        print('BOY')
else:
    if int(A) >= 20:
        print('WOMAN')
    else:
        print('GIRL')
def f():
    a=a

#9460
a, b = map(int,input().split())
def f():
    a ==A
    b ==B
print(f"함수 내부: a = {b}, b = {a}")
print(f"함수 외부: a = {a}, b = {b}")
print(f"함수 내부: a = {b}, b = {a}")
print(f"함수 외부: a = {b}, b = {a}")

#9461
n, m = 0, 0
def f():
    global n, m
    n, m = map(int,input().split())

    if n > m:
        print(n//2, m*2)
    else:
        print(n*2, m//2)
f()

#9462
N = int(input())
M = []
M.append(map(int,input().split()))
for i in range(4):
    print(random.(M))
    
#9179
N = int(input())
print(f"입력받은 정수:",N)

#9180
N = int(input())
print(f"I am {N} years old")

#9181
O = int(input())
Y = int(input())
print(O - Y)

#9182
f = int(input())
s = int(input())
t = int(input())
print(f+s+t)

#9183
n = float(input())
print(f"입력받은 실수: {n}")

#9184
n = float(input())
m = float(input())
print(f"좌표 = ( {n} , {m} )")

#9185
n = int(input())
m = float(input())
print(n,'+',m,'=',n + m)

#9186
n = float(input())
m = float(input())
print(n+5)
print(m-5)

#9187
n, m =map(int,input().split())
print(n, '*', m, '=', n*m)
'''
#9188
x, y = map(int,input().split())
print(y)
print(x)

#9189
n, m, x, y = map(int,input().split())
print("total sum =",n+m+x+y)

#9190
n, m = map(int,input().split())
print(n, "**",m,"=",n**m)

#9191
a, c = map(int,input().split())
b, d = map(int,input().split())
print(a*b+c*d)

#9192
n, h, w = input().split()
print("name:",n)
print("height:",h)
print("weight:",w)

#9193
N, B = input().split()
n, b = input().split()
print(N,"was born in",B)
print(n,"was born in",b)
print(N,"is",int(b)-int(B),"years older than",n)

#9194
l = input()
t, d = input().split()
print('Location:',l)
print('Time:',t,'hours')
print('Distance:',d,'km')

#9354
a = []
for i in range(5):
    A = input()
    a.append(A)
print(a)

#9209
a, b =map(int,input().split())
if a == b:
    print("True")
else:
    print("False")
if a != b:
    print("True")
else:
    print("False")
    