N, M = map(int, input().split())
lst = list(map(int, input().split()))

ans = 0
for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum_v = lst[i] + lst[j] + lst[k]
            if ans < sum_v <= M:
                ans = sum_v
print(ans)