'''
#BJ2766
s =input()
i =int(input())
print(s[i-1])

#BJ2588
a=int(input())
b=input()
print(a * int(b[2]))
print(a * int(b[1]))
print(a * int(b[0]))
print(a * int(b))

#덧셈으로 (6)번
#print(a * int(b[2]) + a * int(b[1])*10 + a * int(b[0]) *100)

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
print(A+B+C)

#BJ10171
# print(''\\    /\\
# )  ( ')
#(  /  )
# \\(__)|'')

#BJ10172
#print(''|\_/|
#|q p|   /}
#( 0 )"""\\
#|"^"`    |
#||_/=\\\\__|'')

#BJ1330
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


H, M = map(int, input().split())
M -= 45
if M < 0:
    M += 60
    H = (H - 1) % 24
print(H, M)

#BJ2739
N=int(input())
for M in range(1,10,1):
    print(f'{N} * {M} =',N*M)

#BJ2741
N=int(input())
print(*range(1,N+1),sep='\n')

#BJ2742
N=int(input())
print(*range(N,0,-1),sep='\n')

#BJ2525
A, B=map(int,input().split())
C=int(input())
if (B+C)%60==0:
    if A+(B+C)//60<24:
        print(A+(B+C)//60, 0)
    else:
        print((A+(B+C)//60)-24,0)
if (B+C)%60 !=0:
    if A+(B+C)//60<24:
        print(A+(B+C)//60,(B+C)%60)
    else:
        print((A+(B+C)//60)-24,(B+C)%60)

'''