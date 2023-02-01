'''
파일 입출력
      입력(input) 기존 파일을 읽어들이는 것
      출력(output)  파일 생성, 내용 추가
'''
'''
file = open('myFile.txt','wt')
print('myFile.txt 파일이 생성되었습니다')
file.close()
'''
with open('../myFile.txt', 'wt') as file:
    print('myFile.txt 파일이 생성되었습니다') #with문,  자동으로 close 해줌