'''
#2072
t = int(input())
S = []
s = 0
for i in range(t):
    w = (map(int,input().split()))
    for j in w:
        if j%2 ==1:
            s += j
    S.append(s)
    s = 0

for k in range(t):
    print(f"#{k+1} {S[k]}")

#6196
a = int(input())
print((a*4)+(a*10)*3+(a*100)*2+(a*1000))

#6204
i = int(input())
print(f"{i}.00 inch => {i*2.54} cm")

#6220
l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
t = int(input())
for i in range(t):
    a = input()
    if a in l:
        print(f"#{i+1} {a} 는 소문자 입니다.")
    else:
        print(f"#{i+1} {a} 는 대문자 입니다.")

#1244
T = int(input())
L = []
for i in range(T):
    n, t = map(int,input().split())
    N = list(n)
    m = max(N)
    M = N.sort(reverse=True)
    for j in N:
        if t == 1:
            if M == N :
                N[len(N)-2],N[-1] = N[-1],N[len(N)-2]
                L.append(N)
            else:
                N[max(N)], N[0] = N[0], N[max(N)]
                L.append(N)
        else:

#6221
L = ['가위','바위','보']
f = L.index(input())
s = L.index(input())
L[0] < L[1] and L[1] < L[2] and L[2] < L[0]
if f == s:
    print('Result : Draw')
elif f > s:
    print('Result : Man1 Win!')
else:
    print('Resilt : Man2 Win!')

#6218
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(f"{i}(은)는 {n}의 약수입니다.")
'''
#2027
print('''#++++
+#+++
++#++
+++#+
++++#''')
