'''
#6308
n=input()
a=int(input())
print(f"{n}(은)는 {100-a+2019}년에 100세가 될 것입니다.")
'''
#4828
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    print(f"#{i+1} {l[-1]-l[0]}")