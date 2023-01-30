'''
지역변수(local variable)
     함수 내부 선언
     내부에만!!! 가능

전역변수(global)
     함수 외부 선언
     내부 외부 가능
'''

gVar = '전역'
def globalAndlocal():
    lVar = '지역'
    print(gVar,'변수입니다') #전역변수 참조만 함
    print(lVar,'변수입니다')

globalAndlocal()



gVAr = '전역'
def globalAndlocal2():
    lVar = '지역'
    gVar = '변경된 전역이 아닌 새로운 지역'  # <- 지역변수임 위의 선언과는 다르다!!!
    print(gVar, '변수입니다')
    print(lVar, '변수입니다')

globalAndlocal2()
print(gVar)  #바꿔줬는데도 전역이라고 나옴

print(' ')

#전역변수 선언
total = 0
def gift(dic, who, money):
    global total #전역변수 total을 사용할것
    total += money
    dic[who] = money #?????????????????????

wedding = {}   #??????????????
gift(wedding, '영희', 5)
gift(wedding, '철수', 6)
gift(wedding, '이모', 7)

print('축의금 명단 : {}'.format(wedding))
print('전체 축의금 : {}'.format(total))