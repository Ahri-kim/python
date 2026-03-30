'''
#9453
N=int(input())
def f(N):
    print(N,'+',10,'=',N+10)
    print(N,'-',10,'=',N-10)
f(N)


#9454
N, M = map(int,input().split())
Y = abs(N-M)
def f():
    print(f'두 수의 합 = {N+M}')
    print(f'두 수의 차 =',Y)
f()

#9455
r=int(input())
def a():
    print(f"{r*r*3.14:.2f}")
a()

#9456
a, b, c = map(int,input().split())

#9377
A=input()
for a in A:
    print(a,end=' ')

#9378
a = input()
A = a[0::2]
X = ' '.join(A)
print(X)

#9456
import sys
a, b, c = map(int,sys.stdin.readline().split())
def f():
    print((a*4)+(b*2)+c)
    print((a*9)+(b*3)+c)
    print((a*25)+(b*5)+c)
f()

#9457
import sys
globalK = int(sys.stdin.readline())
a, b, c = map(int,sys.stdin.readline().split())
def f():
    print(abs(a - globalK))
    print(abs(b - globalK))
    print(abs(c - globalK))
f()

#9379
import sys
w = sys.stdin.readline()
print(w[::-1])

#9694
import sys
N, A = sys.stdin.readline().split()
class In:
    def __init__(self, name, age):
        self.name = name
        self.age = age

b1 = In(N, A)
print(f'My name is {b1.name}.')
print(f'I am {b1.age} years old.')

#9695
n, r, t = input().split()
class Im:
    def __init__(self, name, room, toilet):
        self.name = n
        self.room = r
        self.toilet = t
    
b1 = Im(n, r, t)
print('location:', b1.name)
print('bedrooms:', b1.room)
print('bathrooms:', b1.toilet)

#9696
a, b = input().split()
a1, b1 = input().split()
class P:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)
    def status(self):
        if self.age >= 18:
            return f'{self.name}({self.age}) : adult'
        else:
            return f'{self.name}({self.age}) : child'
p1 = P(a, b)
p2 = P(a1, b1)
print(p1.status())
print(p2.status())
'''
#9697
a1, a2, a3 = input().split()
b1, b2, b3 = input().split()
class B:
    def __init__(self, name, avg, ab, h):
        self.name = name
        self.avg = avg
        self.ab = ab
        self.h = h
    def bs(self):
        print(f'name:{self.name}, AVG:{self.avg}, AB:{self.ab}, H:{self.h}')
h1 = int(a3)/int(a2)
h2 = int(b3)/int(b2)
round(h1,3)
round(h2,3)
p1 = B(a1, h1, a2, a3)
p2 = B(b1, h2, b2, b3)
print(p1.bs())
print(p2.bs())