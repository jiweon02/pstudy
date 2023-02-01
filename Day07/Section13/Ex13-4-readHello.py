'''
r(read mode)
       읽기 전용 모드 / 파일 없으면 에러

경로
      절대경로
      상대경로
           . -> 현재 위치
           .. -> 상위 폴더
'''

file = open('Hello.txt','rt', encoding='UTF-8')
str = file.read()
print(str, end='')
file.close()

'''
with open('Hello.txt','rt') as file:
    str = file.read()
    print(str, end='')
    file.close()
'''
