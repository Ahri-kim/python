'''
#수학적 계산법. 복합중복제거에 부적합.
t=int(input())
s=t*100
l=[]
for i in range(t):
    x,y=map(int,input().split())
    l.append((x,y))
if t!=1:
    for i in range(t-1):
        if abs(l[i][0]-l[i+1][0])>=10:
            pass
        else:
            s-=(10-abs(l[i][0]-l[i+1][0]))*(10-abs(l[i][1]-l[i+1][1]))
print(s)
'''
#직관적인 방법 이차원리스트로 시뮬레이션?느낌.
t=int(input())
l=[[0] * 100 for _ in range(100)]
for i in range(t):
    x,y=map(int,input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            l[i][j] = 1
print(sum(sum(row) for row in l))

#좌표값 저장하는데, 셋으로 자동중복제거.
t = int(input())
l = set()
for _ in range(t):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            l.add((i,j))
print(len(l))