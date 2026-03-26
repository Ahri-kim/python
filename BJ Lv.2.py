#2884
'''H, M=map(int,input().split())
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
        print((A+(B+C)//60)-24,(B+C)%60)'''

#2480
A, B, C=map(int,input().split())
my_list=[A, B, C]
my_list.sort()
if A==B==C:
   print(10000+(A)*1000)
if (A==B or B==C or C==A) and not A==B==C:
    print(1000+my_list[1]*100)
if A!=B!=C:
    print(my_list[-1]*100)