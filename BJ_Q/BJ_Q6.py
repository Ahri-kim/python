'''
#2738
n, m = map(int,input().split())
for i in range(n):
    a = map(int,input().split())

#8958
t = int(input())
L = []
S = 0
n = 0
for i in range(t):
    s = list(input())
    for j in s:
        if s[0] and s[0] == 'O':
            S += 1
            n += 1
        else:
            n += 1            
        if j == 'O' and s[n] != 'X':
            S += (1 + n)
            n += 1
        elif j == 'O' and s[n] == 'X':
            S += 1
            n += 1
        else:
            pass
    L.append(S)
    S = 0
    n = 0
print(*L)

#-------------------------------------------------------

t = int(input())
n = 0
S = 0
L = []
for i in range(t):
    s = list(input())
    for j in s:
        if j == 'O':
            if n != 0:
                n += 1
                S += n
            else:
                S += 1
                n += 1                
        else:
            n = 0
    n = 0
    L.append(S)
    S = 0
for x in L:
    print(x)
'''
#1193
N = int(input())
s = 1
a = 2
i=0
if N > 2:
    while N <= s :
        s += a
        a += 1
    if (a-1)%2 ==0:
        i = (a -1) - (s-N)
    else:
        i = N-s-1
    print( i,'/', a-1)
elif N == 1:
    print(1,'/',1)
else:
    print(1,'/',2)








#N = int(input())
#s = 1
#a = 1 
#while N > a:
#    a += 6 * s
#    s += 1
#print(s)











