'''
#ex)01
def secret():
    message ='이건 나만의 비밀'
    print(message)
    message='함수 내에서는 자유롭게 수정이 가능해요.'
    
def please():
    message = '이렇게 하면 되지?'
    print(message)

message2 = '이것도 비밀'
print(message2)
secret()
please()

#ex)02
message = '나는야 전역 변수'
print(message)

def no_secret():
    global message
    message='이러면 또 지역 변수'
    print(message)

no_secret()
print(message)

#ex)03
f = open('list.txt','w',encoding='utf-8')
f.write('김xx\n')
f.write('정xx\n')
f.write('허xx\n')
f.close()

f = open('list.txt','r',encoding='utf-8')
for line in f:
    print(line, end='')
f.close()

#ex)04
class BlackBox:
    pass

b1 = BlackBox()
b1.name = '까망이'
print(b1.name)
print(isinstance(b1,BlackBox))

#ex)05
class BlackBox:
    def __init__(self,name,price):
        self.name = name
        self.price = price

b1 = BlackBox('까망이',200000)
print(b1.name, b1.price)
b2 = BlackBox('하양이',100000)
print(b2.name, b2.price)

#ex)06
class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def set_travel_mode(self, min):
        print(str(min)+'분 동안 여행모드 ON')
b1 = BlackBox('까망이', 200000)
b1.set_travel_mode(20)
'''
#ex)07
class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def set_travel_mode(self, min):
        print(f'{self.name} {min}분 동안 여행 모드 ON')
b1 = BlackBox('까망이',200000)
b2 = BlackBox('하양이',100000)

b1.set_travel_mode(20)
b2.set_travel_mode(10)
BlackBox.set_travel_mode(b1, 25)

#ex)08
