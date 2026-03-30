'''
#BJ2480
A, B, C=map(int,input().split())
num=[A, B, C]
num.sort()
if num[0] == num[2]:
   print(10000+num[0]*1000)
elif num[0]==num[1] or num[1]==num[2]:
    print(1000+num[1]*100)
else:
    print(num[-1]*100)


#10950
T=int(input())
for x in range(T):
    A, B=map(int,input().split())
    print(A+B)

#1.for _ in range(int(input())):
    A, B = map(int, input().split())
    print(A + B)

#2.sums = [sum(map(int, input().split())) 
for x in range(int(input()))]

for a in sums:
    print(a)

#BJ8393
n=int(input())
print(((n+1)*n)//2)

#BJ25304
X=int(input())
N=int(input())
total = 0
for _ in range(N):
    a, b = map(int,input().split())
    total += a*b

if X == total:
    print('Yes')
else:
    print('No')

#for _ in range(int(input())):
#s1, s2 = {map(int,input().split())for _ in range(int(input()))} #a,b for N
#for x,y in zip(s1, s2):
# sum((x*y for x, y in zip(s1,s2)))
'''