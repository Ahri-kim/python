'''
import math

def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    g = math.gcd(numer, denom)
    numer //= g
    denom //= g
    return [numer, denom]

my_string="hi12392"

L=list(range(0,10))
def solution(my_string):
    return sorted([int(i) for i in my_string if i.isdigit()])

my_str='abc1Addfggg4556b'
n=6

def solution (my_str,n):
    m=[]
    while len(my_str)!=0:
        m.append(my_str[:n])
        my_str=my_str[n:]
    return m

def solution(numbers):
    l = ["zero", "one", "two", "three", "four","five", "six", "seven", "eight", "nine"]
    for i in l:
        numbers = numbers.replace(i, str(l.index(i)))

    answer = int(numbers)
    return answer

def solution(num_str):
    num_str = sum(map(int, num_str))
    answer = num_str
    return answer

emergency=[3,76,24]

def solution(emergency):
    E = sorted(emergency, reverse=True)
    return [E.index(i) + 1 for i in emergency]

dots=[[1, 4], [9, 2], [3, 8], [11, 6]]

def solution(dots):
    r=0
    a=0
    b=1
    L=[]
    for i in range(1,4):
        L.append(abs(dots[r][b]-dots[i][b])/abs(dots[r][a]-dots[i][a]))
        r+=1
    for i in L:
        if L.count(i) > 1:
            answer = print(1)
        else:
            answer = print(0)
    return answer

dots=[[1, 4], [9, 2], [3, 8], [11, 6]]
def solution(dots):
    L = []
    for k in range(3, -1, -1):
        for i in range(k):
            dx = dots[k][0] - dots[i][0]
            dy = dots[k][1] - dots[i][1]
            if dx == 0:
                L.append('ss')
            else:
                L.append(dy / dx)
    for i in L:
        if L.count(i) > 1:
            return 1
    return 0
'''
def solution(age):
    l = [chr(i) for i in range(ord('a'), ord('j') + 1)]
    age=str(age)
    if len(age)==3:
        answer = l[int(age[0])]+l[int(age[1])]+l[int(age[2])]
    elif len(age)==4:
        answer = l[int(age[0])]+l[int(age[1])]+l[int(age[2])]+l[int(age[3])]
    elif len(age)==2:
        answer = l[int(age[0])]+l[int(age[1])]
    else:
        answer = l[int(age[0])]
    return answer