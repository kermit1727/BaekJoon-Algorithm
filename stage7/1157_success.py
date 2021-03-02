string = input()
a_dic = {}
max_a = 0
result_list = []

for i in range(65, 91):
    a_dic[chr(i)] = 0

for C in string:
    for key in a_dic:
        if (C == key or C == key.lower()):
            a_dic[key] += 1

result_list = list(a_dic.values())

if (result_list.count(max(result_list)) == 1):
    for key in a_dic:
        if a_dic[key] == max(result_list):
            max_a = key
            break
else:
    max_a = '?'
    
print(max_a)