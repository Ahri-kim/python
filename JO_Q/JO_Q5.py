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
'''
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

