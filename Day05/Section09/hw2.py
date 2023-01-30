id = None
pwd = None

while True:
    id = input('아이디를 입력하세요(3글자 이상) >>> ')
    if len(id) > 2:
        break
    print('3글자 이상 입력해 주세요')

while True:
    pwd = input('비밀번호를 입역해주세요(영문, 숫자 포함 8글자 이상 >>> ')
    isContainAlpha = False
    isContainNumeric = False

    if len(pwd) < 8:
        print('영문, 숫자 포함 8글자 이상 입력해 주세요')
        continue

    for ch in pwd:
        if ch.isalpha():
            isContainAlpha = True
        elif ch.isnumeric():
            isContainNumeric = True

    if not isContainAlpha:
        print('영문, 숫자 포함 8글자 이상 입력해 주세요')
        continue

    if not isContainNumeric:
        print('영문, 숫자 포함 8글자 이상 입력해 주세요')

    pwdChk = input('비밀번호를 한번 더 입력하세요')
    if pwd != pwdChk:
        print('일치하지 않습니다, 다시 입력해 주세요')
        continue

    break

print('회원가입 완료!')



print('')



#로그인
while True:
    loginid = input('아이디를 입력하세요 >>> ')
    if id == loginid:
        break
    print('아이디가 일치하지 않습니다')

while True:
    loginpwd = input('비밀번호를 입력하세요 >>> ')
    if pwd == loginpwd:
        break
    print('비밀번호가 일치하지 않습니다')



print('로그인 성공!')
print('{}님 환영합니다'.format(id))