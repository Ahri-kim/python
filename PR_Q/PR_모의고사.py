def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    d = [0,0,0]
    for i in range(len(answers)):
        if a[i % len(a)] == answers[i]:
            d[0] += 1
    for i in range(len(answers)):
        if b[i % len(b)] == answers[i]:
            d[1] += 1
    for i in range(len(answers)):
        if c[i % len(c)] == answers[i]:
            d[2] += 1
    r = []
    for i in range(len(d)):
        if d[i] == max(d):
            r.append(i + 1)
    r.sort()
    return r

#-------------------------------------------------------------------------------
'''
answers = [1,2,3,4,5]
a=[1,2,3,4,5]
b=[2,1,2,3,2,4,2,5]
c=[3,3,1,1,2,2,4,4,5,5]
d=[0,0,0]
for i in range(len(answers)):
    if i>4:
        i=i%5
    if a[i] == answers[i]:
        d[0] += 1
for i in range(len(answers)):
    if i>7:
        i=i%7
    if b[i] == answers[i]:
        d[1] += 1
for i in range(len(answers)):
    if i>10:
        i=i%10
    if c[i] == answers[i]:
        d[2] += 1        
if d.count(max(d))==1:        
    p=d.index(max(d))+1
    print(f"가장 문제를 많이 맞힌 사람은 수포자{p}입니다.")
elif d.count(max(d))==2:
    p=d.index(max(d))+1
    d[p-1]=0
    q=d.index(max(d))+1
    print(f"가장 문제를 많이 맞힌 사람은 수포자{p}와 {q}입니다.")
else:
    print(f"모든 사람이 {max(d)}문제씩을 맞췄습니다.")

'''
#-----------------------------------------------------------------------------------------------------------------
def solution(answers):
    m = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [[b[i % len(b)] - a for i, a in enumerate(answers)].count(0) for j, b in enumerate(m)]
    return [i + 1 for i, a in enumerate(s) if a >= max(s)]

