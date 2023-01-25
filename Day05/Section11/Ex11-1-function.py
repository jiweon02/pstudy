'''
함수
      하나의 특별한 목적의 작업을 수행하기 위해
      독립적으로 설계된 프로그램 코드의 집합

def함수이름(매개변수)
      코드 실행문
      return 반환값
'''
# welcome() 함수 정의(실행X)
def welcome():
    print('Hello python')
    print('Nice to meet you!')   #매개변수 없고 리턴 역시 없다

welcome()

#매개변수 있고 리턴 없는 함수
def introduce(name, age):
    print('내 이름은 {}이고, 나이는 {}살 입니다.'.format(name,age))
introduce("현지원",17)



#가변 매개변수 함수
def show(*args):
    for item in args:
        print(item)
show('python')
show('jiweon','jinwoo')

#매개변수가 없고 리턴값이 있는 함수
def address():
    str = '우편번호 12345\n'
    str += '서울시 영등포구 여의도동'
    return str

result = address()

print(result)

#매개변수가 있고 리턴도 있는 함수
def plus(num1, num2):
    return num1+num2

result = plus(5,7)
print(result)
print(plus(81,6))

area = 0
def rMove():
    global area
    area += 4

def lMove():
    global area
    area += 4
rMove()
rMove()
rMove()
lMove()
lMove()
print('유닛이 오른쪽으로 {}칸 이동했습니다'.format(area))