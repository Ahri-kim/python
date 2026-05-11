'''
#6308
n=input()
a=int(input())
print(f"{n}(은)는 {100-a+2019}년에 100세가 될 것입니다.")

#4828
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    print(f"#{i+1} {l[-1]-l[0]}")

#4880
T=int(input())
R=2, S=1, P=3
R>S, R<P, S>P
for i in range(T):
    N=int(input())
    l=list(map(int,input().split()))
    mid=len(l)//2
    while True:
        for j in l[:mid-1]:
            if l[j]>l[j+1]:
                l[j+1] = 
            else:
                l.pop(l[j])
        for k in range(mid,len(l)):
            if l[k]>l[k+1]:
                l.pop(k+1)
            else:
                l.pop(k)
        if len(l)==2:

            False
            break

#4873
T=int(input())
for i in range(T):
    s=list(input())
    t=0
    while t<len(s)-1:
        if s[t] == s[t+1]:
            del s[t:t+2]
            if t>0:
                t-=1
        else:
            t+=1
    print(f"#{i+1} {len(s)}")
'''
#4864
T=int(input())
for i in range(T):
    s1=input()
    s2=input()
    if s1 in s2:
        print(f"#{i+1} 1")
    else:
        print(f"#{i+1} 0")