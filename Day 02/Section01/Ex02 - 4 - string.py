'''
문자열(string)
   하나 이상 연속된 문자(character)들의 나열
   핑;썬에서 문자열 자료명은 큰 따옴표(")
   또는 작은 따옴표 (') 사이에 위치
'''

#'hello'와 'hello'  동일
print("hello" == "hello") #값이 같으면 true 반환

'''
변수에 문자열 할당
'''

a = "hello"
print(a)


'''
여러줄 문자열
   세개의 따옴표를 사용하여 변수에 여러개의 문자열 할당
'''

a = """피카츄, 라이츄, 파이리, 꼬부기, 버터풀, 아도란"""
print(a)

'''
문자 배열 => 문자열
     문자열 인덱싱(indexing)
    h  e  l  l  o <== 문자열
    0  1  2  3  4 <== 인덱스
   -5 -4 -3 -2 -1 <== 마이너스 인덱스 (얜 파이썬만 됨)
'''

a = "hello"
print(a[1])
print(a[1] == a[-4])

'''
문자열 슬라이싱
     슬라이싱 구문을 사용하여 문자 번위 반환 가능
     문자열의 일부를 반환하려면 시작 인덱스와 끝 인덱스를 쿨론으로 구분
'''
b = "hello, world"
print(b[2:5]) #2부터 5 이전까지
print(b[:5]) #처음부터 5 이전까지
print(b[2:]) #2부터 끝까지

a = "hello, world"
print(a.lower()) #문자를 전부 소문자로
print(a.upper()) #문자를 전부 대문자로

a = "hello, world"
print(a.replace`

#문자열 연결
a = "hello"
b = "world"
c = a + b
print(c)

a = "age"
b = 15
c = a + "/" + str(b)
print(c)