'''
논리 연산자
     관계연산자와 함께 사용
     2개 이상의 항을 논리적으로 연결할 때 사용
     예) and or not
'''

a = 10
b = 0
print('{} > 0 and {} > 0 : {}'.format(a, b, a>0 and b>0))
print('{} > 0 or {} > 0 : {}'.format(a, b, a>0 and b>0))
print('not {} : {}'.format(a, not a))
print('not {} : {}'.format(b, not b))