'''
#JO9227
a ,b=map(int,input().split())
print(max(a,b))

JO#9266
N=int(input())
for N in range(10,N+1,10):
    print(N)

JO#9267
N=int(input())
print(*range(N,0,-1)

ex.01)
max=25
weight=0
item=3

while weight + item <= max:
    weight+= item
    print('짐을 추가합니다.')
print(f'총 무게는 {weight}입니다.')

ex.02)
drama = ['시즌1','시즌2','시즌3','시즌4','시즌5']
for x in drama:
    if x=='시즌3':
        print('재미 없대, 그만 보자')
        continue
    print(f'{x}시청')

ex.03)
for x in range(10):
    if x %2==1:
        continue
    print(x)

ex.04)
products = ['JOA-2020','JOA-2021','SIRO-2021','SIRO-2022']
recall =[]
for p in products:
    if p.startswith('SIRO'):
        recall.append(p)

print(recall)

ex.05)
def my_function():
    print('새로운')
    print('함수를')
    print('만들었어요.')
my_function()

ex.06)
def show_price():
    print(f'{customer}고객님 감성커트 가격은 15000원입니다.')


ex.07)
def get_price():
    return 15000

price = get_price()
print(f'커트 가격은 {price}원 입니다.')

ex.08)
def get_price(is_vip):
    if is_vip == True:
        return 10000
    else:
        return 15000

price = get_price(True)
print(f'커트 가격은 {price}원 입니다.')
price = get_price(False)
print(f'커트 가격은 {price}원 입니다.')

ex.09)
def get_price(is_vip=False):
    if is_vip ==True:
        return 10000
    else:
        return 15000

price1 =get_price(True)
print(price1)
price2 =get_price()
print(price2)
price3 =get_price()
print(price3)
price4 =get_price()

ex.10)
def visit(today,*customers):
    print(today)
    for customers in customers:
        print(customers)

visit('2026.03.27','나장발')
visit('2026.03.27','나장발','나수염','나김리', '강승진')

ex.11)'''