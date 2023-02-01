'''
패키지
      모듈 상위 개념
      모듈의 집합!
패키지 설치
    console > pip install 패키지명
" 삭제
   console > pip uninstall 패키지명
'''
#행렬 연산 관련 패키지
import numpy as np

print(np.sum([1,2,3,4,5]))

a = np.array([1,2,3])
b = np.array([4,5,6])


#각 요소 더하기
c = a + b
c = np.add(a,b)
print(c)

#각 요소 빼기
c = a - b
c = np.subtract(a,b)
print(c)


''' 집가서 챙길 리스트

1. 비행기에 가져갈 가방 
     지갑 아이패드 휴대폰
     여권 비행기 자료? 그 파일에 담겨 있는거
     목배게 그냥 챙기기 내일은 안경 끼고 가기 (안경 케이스 챙기기
     
2. 케리어에 더 넣을 것들
     수영복 

3. 기타 준비할 것
    플레이리스트 및 영상 다운 받기 
    휴대폰이랑 아이패드 다 풀 충전!
    '''

# 각 요소 곱하기
c = a*b
c = np.multiply(a,b)
print(c)

# 각 요소 나누기
c = a / b
c = np.divide(a,b)
print(c)

