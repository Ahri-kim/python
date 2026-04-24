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

#1193
n = int(input())
f = 1  # 층수
m = 0  # 대빵
while m+f < n:
    m += f
    f += 1
l = n-m
if f % 2 == 0: #짝수 층(왼-오)
    x = l
    y = f-l+1
else:         #홀수 층(오-왼)
    x = f-l+1
    y = l
print(f"{x}/{y}")

#1110
n = input()
if n != '0' and len(n) == 1:
    n = list(n)
    n.insert(0, '0')
elif n == '0':
    print(1)
else:
    pass

if n != '0':
    n = list(n)
    N = int(n[0]) * 10 + int(n[1])
    t = 0
    s = 0
    l = []
    while t != N:
        t = int(n[0]) + int(n[1])
        s += 1
        l.append(str(t)[-1])
        n[0], n[1] = n[1], l[0]
        l = []
        t = int(n[0]) * 10 + int(n[1])
    print(s)
else:
    pass

#2440
n = int(input())
for i in range(n,0,-1):
    print('*'*i)

#2441
n = int(input())
for i in range(n,0,-1):
    print(f"{'*'*i:>{n}}")

#2739
n = int(input())
for i in range(1,10,1):
    print(f"{n} * {i} = {n*i}")


#9012
n = int(input())
for i in range(n):
    S = input()
    for j in range(len(S)):
        S = S.replace("()","",1)
        if S =='':
            break
    if S =='':
        print('YES')
    else:
        print('NO')    
'''