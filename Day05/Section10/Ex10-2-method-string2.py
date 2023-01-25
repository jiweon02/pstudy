# join() 메소드
s = '-'.join('python')
print(s)

s = '+'.join(['a','b','c','d','e'])
print(s)

s = ' '.join(['a','b','c','d','e'])
print(s)

#split() method
s = 'Life is too short'
result = s.split()
print(result)  #띄어쓰기 기준으로 list로 반환함

s = '010-1111-2222'
result = s.split('-')
print(result)
print(result[2])

data = '현지원|17|학생'
result = data.split('|')
print(result)
print('이름: {}'.format(result[0]))

#replace() method
s = "life is too short"
result = s.replace('short','long')
print(result)

#strip(), lstrip(), rstrip() 공백제거
s = '         apple'
result = s.lstrip() #delete left side's blank
print(result)

s = 'apple      '
result = s.rstrip() #delete right side's blank
print(result)

s = '           apple      '
result = s.strip() #both side
print(result)

s = ' a p p l e '
print(s)
result = s.strip()
print(result)
#전체 공백제거
result = s.replace(' ','')
print(result)
