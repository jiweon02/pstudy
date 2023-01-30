'''
time 모듈
     시간 처리에 관련된 time 모듈
'''

import time
print(time.time())  #1970 1월 1일 0시 0분 0초부터 현재까지 경과 시간을 반환 #마이크로초까지 반환

#ctime() 함수 - 인수로  전달된 time 시간 형식을 갖춰 반환
print(time.ctime(time.time()))

#인수로 전달된 날짜와 지시자를 이용하여 형식을 갖춘
#날짜 데이터를 문자열로 반환

print(time.strftime('%Y-%m-%d %H:%M:%S'))

#한국어 인코딩 문제 시 이렇게!
print(
    time.strftime(
        '%Y년 %m월 %d일'
        .encode('unicode-escape')
        .decode()
    ).encode().decode('unicode-escape')
)



# 인자 초만큼 시스템 일시 중지
time.sleep(1)



