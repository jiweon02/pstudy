'''
method
    특정 개체가 가지고 있는 함수를 의미
    객체.메소드() 이런식으로 사용 ㄱㄴ
'''

#string 객체
print("10자리 폭 왼쪽 정렬 '{:<10d}'".format(123))
print("10자리 폭 오른쪽 정렬 '{:>10d}'".format(123))
print("10자리 폭 가운데 정렬 '{:^10d}'".format(123))
print()
print("10자리 폭 왼쪽 정렬 채움 문자 '{:*<10d}'".format(123))
print("10자리 폭 오른쪽 정렬 채움 문자 '{:*>10d}'".format(123))
print("10자리 폭 가운데 정렬 채움 문자 '{:*^10d}'".format(123))

#count() 매서드

s = ' 내가 그린 기린 그림은 목이 긴 기린 그림이고, 네가 그린 기린 그림은 목 짧은 기린 그림이다'
result = s.count('기린')
print(result)

s = 'best of best'
result = s.count('best',5)
print(result)


#find() 메소드 - 위치한 인덱스 번호 반환
s = 'apple'
result = s.find('p')
print(result)

result = s.find('z')
print(result)      # 없는 값 -1 로 밚환

if result == -1:
    print('존재하지 않는 문자입니다')

s = "best of best"
result = s.find('best',5)
print(result)
result = s.find('best', -7)
print(result)

#index() - find() 메소드와 같지만 문자열이 존재하지 않을 경우 에러가 발생한다
s = 'apple'
# result = s.index('z')
# print(result)     - 문자열이 없어 에러 발생















