string = input()
string = string.upper()
alpa_list = [chr(i) for i in range(65, 91)]
result = []

for i in alpa_list:
    result.append(string.count(i))

if result.count(max(result)) > 1:
    print("?")
else:
    print(alpa_list[result.index(max(result))])
