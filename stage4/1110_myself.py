num = input()
start = int(num)
loop = 0
sum = 0

if (int(num)) < 10:
    num = '0' + num

while True:
    loop += 1
    sum = int(num[0]) + int(num[1])

    if (sum < 10):
        num = num[1] + str(sum)
    else:
        num = num[1] + str(sum)[1]

    if (int(num) == start):
        print(loop)
        break

