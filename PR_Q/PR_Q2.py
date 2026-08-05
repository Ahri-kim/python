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

n=420
def solution(n):
    l=[]
    i = 2
    while i <= n:
        if n % i == 0:
            l.append(i)
            n //= i
        else:
            i += 1
    return sorted(set(l))
    

def solution(s):
    s = s.split()
    S = 0
    for i in range(len(s)):
        if s[i] != 'Z':
            S += int(s[i])
        else:
            S -= int(s[i-1])
    return S

def solution(numbers):
    return sum(numbers)/len(numbers)

import math

def solution(balls, share):
    return math.factorial(balls) // (
        math.factorial(share) * math.factorial(balls-share)
    )

keyinput=["left", "right", "up", "right", "right"]
board=[11, 11]

def solution(keyinput, board):
    x, y = 0, 0
    max_x = board[0] // 2
    max_y = board[1] // 2
    for key in keyinput:
        if key == "up" and y < max_y:
            y += 1
        elif key == "down" and y > -max_y:
            y -= 1
        elif key == "left" and x > -max_x:
            x -= 1
        elif key == "right" and x < max_x:
            x += 1
    return [x, y]

cipher="dfjardstddetckdaccccdegk"
code=4
def solution(cipher, code):
    return cipher[code-1::code]


import math
def solution(n):
    return n // math.gcd(n, 6)

def solution(my_string, n):
    return ''.join(map(lambda x: x * n, my_string))

def solution(array):
    return max(enumerate(array), key=lambda x:x[1])[::-1]