N = int(input())

ans = N
for i in range(2, N):
    cnt = N//i - (i-1)
    if cnt < 1:
        break
    ans += cnt
print(ans)
