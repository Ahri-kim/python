'''

#9153
print('Hello Jungol!')

#9201
a=int(input())
b=int(input())
print(a ,'+',b ,'=',a + b)
print(a ,'-',b ,'=',a - b)
print(a ,'*',b ,'=',a * b)
print(a ,'/',b ,'=',a / b)
print(a ,'//',b ,'=',a // b)
print(a ,'%',b ,'=',a % b)
print(a ,'**',b ,'=',a ** b)


#9204
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
g=int(input())
print(a+2, b-2, c*2, d/2, e//2, f%2, g**2)

#9205
a=int(input())
print(a)
print(a+10)

#9202
a ,b =map(int,input().split())
print(a,'/',b,'=',a//b,'...',a%b)

#9203
a, b, c =map(int,input().split())
print('sum =',a+b+c)
print('avg =',(a+b+c)//3)

#9206
a=int(input())
b=int(input())
print(a-10,'+',b*2,'=',(a-10) + (b*2))

#9207
a, b =map(int,input().split())
print(a%2,b+10,(a%2)+b+10)

#9208
N=int(input())
A, B=map(int,input().split())
print(N==A, N==B, N!=A, N!=B)

#9223
N = int(input())
if N > 10:
    print('Big')

#9224
N =int(input())
print(N)
if N <  0:
    print("MINUS")


#9225
N = int(input())
M = int(input())
print(N + M)
if N%2 ==1:
    print('ODD')
elif M%2 ==1:
    print('ODD')

#9226
a, b = map(int, input().split())

print(min(a, b))
print(max(a, b))

#JO9256
print(*range(1,101))

#JO9257
print(*range(1,5001))

#JO9258
print(*range(3,301),sep='\n')

#JO9259
print(*range(5,2001,5))

#JO9260
print(*range(2,51,2),sep='\n')

#JO9261
N=int(input())
print(*range(1,N+1))

#JO9262
N=int(input())
print(*range(5,N+1),sep='\n')

#JO9263
N=int(input())
print(*range(5,N+1,2),sep='\n')

#JO9264
N=int(input())
print(*range(2,N+1,2))

#JO9265
N=int(input())
print(*range(-10,N+1))

#JO9266
N=int(input())
for N in range(10,N+1,10):
    print(N)

#9267
N=int(input())
print(*range(N,0,-1))

#9450
def m_f():
#    print(''=========================
#line 함수를 호출하였습니다.
#line 함수를 다시 호출합니다.
#========================='')
m_f()


#JO9451
def f():
    print("~!@#$%^&*()_+")
a=int(input())
for _ in range(a):
    f()

#JO9452
N, M=map(int,input().split())
def f():
    print('Hello')
for _ in range(N):
    f()
for _ in range(M):
    f()
'''