'''#9201
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
a, b =map(int,input().split())
if a>b:
    print(b)
    print(a)
elif a<b:
    print(a)
    print(b)

#BJ18108
y=int(input())
print(y-543)

#BJ10430
A, B, C = map(int,input().split())
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)

#BJ11382
A, B, C =map(int,input().split())
print(A+B+C)'''

#BJ10171
#print('''\\    /\\
# )  ( ')
#(  /  )
# \\(__)|''')

 #BJ10172
#print('''|\_/|
#|q p|   /}
#( 0 )"""\\
#|"^"`    |
#||_/=\\\\__|''')

'''#BJ1330
A, B=map(int,input().split())
if A>B:
    print('>')
elif A<B:
    print('<')
elif A == B:
    print("==")

#BJ9498
a = int(input())
if 100>=a>=90:
    print('A')
elif 90>a>=80:
    print('B')
elif 80>a>=70:
    print('C')
elif 70>a>=60:
    print('D')
elif 60>a>=0:
    print('F')

#BJ2753
a=int(input())
if a%4==0 and a%100 !=0 or a%400 ==0:
    print(1)
else:
    print(0)

#BJ14681
x=int(input())
y=int(input())
if x>0 and y>0:
    print(1)
elif x>0 and y<0:
    print(4)
elif x<0 and y>0:
    print(2)
elif x<0 and y<0:
    print(3)

#BJ2884
H, M=map(int,input().split())
if 45<=M<=59:
    print(H,M-45)
elif M<45:
    if H-1<0:
        print(23,M+15)
    else:
        print(H-1,M+15)


#BJ2739
N=int(input())
for M in range(1,10,1):
    print(f'{N} * {M} =',N*M)

#JO9256
print(*range(1,101))

#JO9257
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
print(*range(-10,N+1))'''