string = input()    # 입력 값 수신

alphabat_list = [chr(i) for i in range(65, 91)]    # 대문자 리스트 생성
result = [0 for i in range(26)]    # 알파벳 개수 리스트 생성
max_num = 0 

for C in string:
    for c in range(65, 91):
        if (C == chr(c) or C == chr(c+32)):
            result[alphabat_list.index(chr(c))] += 1

for i in result:
    if (i != 0 and max_num == i):
        max_num = "?"
        break
        
    if(i > max_num):
        max_num = i

if (max_num == "?"):
    print(max_num)
else:
    print(alphabat_list[result.index(max_num)])