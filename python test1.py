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