n = int(input())    # 정수 입력받음
m = n               # 초기값 저장
i = 0               # 사이클 횟수

while True:
    m = m % 10 * 10 + (m % 10 + m // 10) % 10
    i += 1

    if m == n:
        break

print(i)