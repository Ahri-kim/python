'''my_list=['오예스','몽쉘','초코파이','초코파이','초코파이']
print(my_list)
my_set=set[str](my_list)
print(my_set)
my_list=list(my_set)
print(my_list)

my_list=['오예스','몽쉘','초코파이','초코파이','초코파이']
my_dic=dict.fromkeys(my_list)
print(my_dic)
my_list = list(my_dic)
print(my_list)

today='일요일'
if today=='일요일':
   print('게임 한 판')
else:
    print('폰 5분만')
print('공부 시작')

today = '토요일'
if today == '일요일':
    print('게임 한 판')
elif today =='토요일':
    print('폰 5분만')
else:
    print('물 한잔')
print('공부 시작')

yellow_card=0
foul=False
if foul:
    yellow_card+=1
    if yellow_card==2:
        print('경고 누적 퇴장')
    else:
        print('휴..조심해야지')
else:
    print('주의')

min=35
if min > 20:
    print('게임 많이 했네?')
    if min > 40:
        print('당장 안 꺼?')
else:
    print('뭐 해?')

for x in range(10):
    print(f'팔 벌려 뛰기 {x+1}회')

for n in range(1,31,10):
    print(f'{n}번은 {n}번부터 {n+9}번까지 모아줘')

my_list = [1, 2, 3, 4, 5, 6]
for x in my_list:
    print(x)

my_tuple={1, 2, 3, 4, 5, 6}
for x in my_tuple:
    print(x)
    

my_set={'돈가스','보쌈','제육덮밥'}
print(my_set)
#print(my_set[1])
#my_set[1]='빅파이'

#딕셔너리
person={'이름':'나귀욤','나이':'7세', '키':120,'몸무게':23}
print(person['이름'])
print(person['나이'])
#print(person['별명'])
print(person.get('별명'))
person['최종학력']='유치원'
print(person)
person['키']=130
print(person)
person.update({'키':140,'몸무게':26})
print(person)
person.pop('몸무게')
print(person)
person.clear()
print(person)

'''

person ={'이름':'나귀욤', '나이':'7', '키':'120', '몸무게':'23'}
for v in person.values():
    print(v)
for k in person.keys():
    print(k)
for k,v in person.items():
    print(k,v)