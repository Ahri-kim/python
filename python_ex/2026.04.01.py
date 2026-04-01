'''
#ex)01
num1 = 10
num2 = 5
try:
    #print('num1 / num2')
    result = num1 / num2
    print(f'연산 결과는{result}입니다.')
    #print(result)
except ZeroDivisionError:
    print('0으로 나눌 수 없어요.')
except TypeError:
    print('값의 형태가 이상해요.')
except Exception as err:
    print('에러가 발생했어요:',err)
#finally:
#    print('수행종료')

#ex)02
import goodjob
goodjob.say()

#ex)03
import random
print(random.random)
'''
#ex)04
import ex04.goodjod
