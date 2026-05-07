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
'''
def solution(numbers):
    l = ["zero", "one", "two", "three", "four","five", "six", "seven", "eight", "nine"]
    for i in l:
        numbers = numbers.replace(i, str(l.index(i)))

    answer = int(numbers)
    return answer
