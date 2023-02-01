with open('Hello.txt', 'rt', encoding='UTF-8') as file:
    line_list = file.readlines() #이케 하면 리스트로 뽑힘
    print(line_list)
    for line in line_list:
        print(line, end='')

