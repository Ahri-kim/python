'''
#2738
n, m = map(int,input().split())
for i in range(n):
    a = map(int,input().split())
'''
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
'''
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