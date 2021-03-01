n, x = map(int, input().split())
nums = [int(i) for i in input().split()]

for num in nums:
    if num < x:
        print(num, end=" ")
