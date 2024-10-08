def dfs(n, sm):
    global ans
    # 종료 조건
    if n >= N:
        ans = max(ans, sm)
        return

    # 재귀 하부 호출
    if n + T[n] <= N:   # 상담 하는 경우(퇴사 전 완료 가능할 때만 상담)
        dfs(n+T[n], sm+P[n])
    dfs(n+1, sm)        # 상담 하지 않는 경우(항상 가능)

N = int(input())
T = [0]*N
P = [0]*N
for i in range(N):
    T[i], P[i] = map(int, input().split())

ans = 0
dfs(0, 0)
print(ans)