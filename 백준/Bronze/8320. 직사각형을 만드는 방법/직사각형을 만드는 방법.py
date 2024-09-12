N = int(input())

ans = 0
for i in range(1, N+1):     # i : 세로
    for j in range(i, N+1): # j : 가로
        if i*j <= N:
            ans += 1
print(ans)