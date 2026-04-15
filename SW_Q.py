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
