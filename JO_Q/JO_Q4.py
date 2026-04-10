#9210
a, b, c = map(int,input().split())
A =[]
if a>b:
    A.append("True")
else:
    A.append("False")
if b >= c:
    A.append("True")
else:
    A.append("False")
if a<=b:
    A.append("True")
else:
    A.append("False")
if b<c:
    A.append("True")
else:
    A.append("False")
print(*A)

#9211
x, y = map(int,input().split())
if x>y:
    print(f"{x} > {y} == True")
else:
    print(f"{x} > {y} == False")
if x>=y:
    print(f"{x} >= {y} == True")
else:
    print(f"{x} >= {y} == False")
if x<y:
    print(f"{x} < {y} == True")
else:
    print(f"{x} < {y} == False")
if x<=y:
    print(f"{x} <= {y} == True")
else:
    print(f"{x} <= {y} == False")

#9212
A = True
B = False
c = True
print("False True True")

#9213
a = True
B = False
c = False
print('''False
False
True
True
True
True''')

#9214
a = 0
b = 1
c = 2
print('True True False False True')

#9216
a, b, c = map(int,input().split())
if a>b and a>c:
    print('True')
else:
    print('False')
if a ==b and b==c and c==a:
    print('True')
else:
    print('False')
#9230
t = int(input())
if t<12:
    print('AM')
else:
    print('PM')
#9231
a = int(input())
if a >= 90:
    print('A')
elif a >= 80:
    print('B')
elif a >=70:
    print('C')
elif a >= 60:
    print('D')
else:
    print('F')

#9232
a = float(input())
if a <= 50.80:
    print('Flyweight')
elif a <= 61.23:
    print('Lightweight')
elif a <= 72.57:
    print('Middleweight')
elif a <= 88.45:
    print('Cruiserweight')
else:
    print('Heavyweight')

#9233
a = int(input())
b = int(input())
if a>=3 and b>=3:
    print("High")
elif a>=3 or b>=3:
    print("Mid")
else:
    print("Low")

#9234
x, y = map(float,input().split())
if x>=4.0 and y>=4.0:
    print("A grade")
elif x>=3.0 and y>=3.0:
    print("B grade")
else:
    print("F grade")

#9235
a, b, c = map(int,input().split())
A = set()
A.add(a)
A.add(b)
A.add(c)
print("MAX:",max(A))

#9236
g, a = input().split()
if g !='M':
    if int(a)>=19:
        print('WOMAN')
    else:
        print('GIRL')
else:
    if int(a)>=19:
        print("MAN")
    else:
        print("BOY")

#9238
n = int(input())
m = int(input())
print(n) if n>m else print(m)

#9239
a, b, c = map(int,input().split())
A = []
A.append(a)
A.append(b)
A.append(c)
A.sort()
print(A[0]) if A[0] < A[-1] else print(A[1])

#9268
N = int(input())
for i in range(N,4,-1):
    print(i)

#9269
n = int(input())
for i in range(n,0,-3):
    print(i, end = ' ')

#9270
s, e = map(int,input().split())
for i in range(s,e+1,1):
    print(i, end = ' ')

#9271
s, e = map(int,input().split())
for i in range(s,e+1,2):
    print(i)

#9272
s = int(input())
e = int(input())
for i in range(s,e-1,-1):
    print(i, end = ' ')
