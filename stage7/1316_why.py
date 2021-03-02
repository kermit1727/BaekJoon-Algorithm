loop = int(input())
t = loop
now_c = ''
past_c = []

for i in range(loop):
    s = input()
    now_c = s[0]
    
    for j in s:
        if(past_c.count(j) == 0):
            past_c.append(j)
            now_c = j
        elif (now_c != j and past_c.count(j) > 0):
            t -= 1
            break
    past_c.clear()

print(t)