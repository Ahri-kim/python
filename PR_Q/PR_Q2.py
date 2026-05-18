'''
def solution(array):
    array.sort()
    return array[len(array)//2]

def solution(array):
    return sorted(array)[len(array)//2]    


i, j, k, c = 10, 50, 5, 0
for i in range(i, j+1):
    if str(k) in str(i):
        c+=str(i).count(str(k))

sum(str(x).count(str(k)) for x in range(i, j + 1))

array=[1,2,3,3,3,4]

l=[array.count(x) for x in array]
if len(l) != 1 and l.count(max(l)) > max(l):
    print(-1)
else:
    print(array[l.index(max(l))])

myString="dxccxbbbxaaaa"

def solution(myString):
    myString=myString.replace('x',' ')
    l=myString.split()
    return sorted(l)

def solution(myString):
    return sorted(myString.replace('x', ' ').split())

'''
def solution(money):
    return money//5500 , money%5500

def solution(price):
    if price >= 500000: return int(price*0.8)
    if price >= 300000: return int(price*0.9)
    if price >= 100000: return int(price*0.95)
    return price

def solution(s):
    s = sorted(s)
    answer = ''
    for i in s:
        if s.count(i) == 1:
            answer += i
    return answer

def solution(before, after):
    return int(sorted(before) == sorted(after))