'''
file 객체 read() -> 전체 읽어보기
         read(인자값) -> 인자값 만큼 읽어오기
'''

file = open('Hello.txt', 'rt', encoding='UTF-8')
while True:
    str = file.read(5)

    if not str: #읽을 값이 없으면 True
        break
    print(str,end='')

file.close()