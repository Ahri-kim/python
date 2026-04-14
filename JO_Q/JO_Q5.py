'''
#9273
i = 0
s = 0
while i < 10:
    i += 1
    s += i
print(s)

#9274
n = int(input())
s = 0
i = 0
while i > n:
    s += i
    i += 1
print(s) 

#9700
class P:
    def __init__(self,m_h, m_w, f_h, f_w):
        self.m_h = m_h
        self.m_w = m_w
        self.f_h = f_h
        self.f_w = f_w

m_h, m_w = map(float,input("당신의 키와 몸무게를 입력하세요.").split())
f_h, f_w = map(float,input("친구의 키와 몸무게를 입력하세요.").split())
m_h = int(m_h)
f_h = int(f_h)
print(f"my 키: {m_h}, 몸무게: {m_w}")
print(f"friend 키: {f_h}, 몸무게: {f_w}")
print(f"plus 키: {m_h + f_h}, 몸무게: {m_w + f_w}")
print(f"minus 키: {abs(m_h - f_h)}, 몸무게: {abs(m_w - f_w):.2}")
print(f"avg 키: {(m_h + f_h)/2}, 몸무게: {(m_w + f_w)/2}")

#9355
a = []
for i in range(5):
    a.append(int(input()))
print(a)
print(*a)

#9356
a =[1,2,3,4,5]
print('last:',a[-1])
a = [1, 2, 3, 4]
print(a)
print("len: 4")
print()
print("second: 2")
a=[1, 3, 4]
print(a)
print('len: 3')

#9357
a = []
for i in range(5):
    a.append(int(input()))
print(a)
print(a[0:3])

#9358
A = []
for i in range(5):
    A.append(int(input()))
print(A[-1] + A[3])

#9276
i = 1
while 0 <= i <=100:
    i = int(input())
    if 0 <= i <= 100:
        print(f"Score: {i}")
    else:
        break

#9277
K = 1
while K !=0:
    K = float(input())
    if K > 0:
        print("positive")
    elif K < 0:
        print("negative")
    else:
        break

#9278
l =['one', 'two', 'three']
i = 0
while i < 4:
    i = int(input())
    if  1 <= i < 4:
        print(l[i-1])
    else:
        break

#9279
for i in range(501):
    if i%3 == 0:
        continue
    print(i,end=' ')

#9280
n = int(input())
for i in range(1,5):
    if i == n:
        continue
    print(i)

#9281
i = 1
s = 0
while i !=0:
    i = int(input())
    if i < 0:
        continue
    else:
        s += i
print(s)

#9282
i = 1
s = 0
c = 0
while i != 0:
    i = int(input())
    if i<0 or i>100:
        continue
    else:
        s += i
        c += 1
print(f"count = {c-1}")
print(f"total = {s}")
print(f"avg = {s//(c-1)}")

#9294
for i in range(3,100,1):
    print(i,end=' ')

#9295
s, e = map(int,input().split())
for i in range(s,e+1,1):
    print(i,end='   ')

#9296
for i in range(5,56,2):
    print(i,end=' ')

#9297
s, e = map(int,input().split())
for i in range(s,e+1,2):
    print(i,end=' ')

#9298
s = int(input())
e = int(input())
k = int(input())
for i in range(s, e+1,k):
    print(i)

#9299
for i in range(99,2,-2):
    print(i,end=' ')

#9300
s, e =map(int,input().split())
if s%2 ==0:
    s = s - 1
else:
    s=s

for i in range(s,e-1,-2):
    print(i)

#9301
s, e = map(int,input().split())
k = int(input())
for i in range(s,e-1,-k):
    print(i,end=' ')
'''
#9302
n = int(input())
print(sum(range(1, n + 1)))

#9303
n = int(input())
print(sum(range(10, n + 1)))

#9304
n = int(input())
print(n//3)

#7102
c = 0
s = 0
n = int(input())
for i in range(n):
    j = int(input())
    if j % 2 == 0:
        c += 1
    else:
        s += j
print(s, c)