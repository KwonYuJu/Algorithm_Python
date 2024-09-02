N, X = map(int, input().split())
A = list(map(int, input().split()))
nums = []
for i in A:
    if i < X:
        nums.append(i)
print(*nums)