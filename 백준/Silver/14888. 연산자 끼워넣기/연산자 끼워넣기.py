def dfs(n, sm, add, sub, mul, div):
    global mn, mx
    # 결과값, 중간값 범위
    if sm < int(-1e9) or sm > int(1e9):
        return

    # 종료 조건 (정답 처리)
    if n == N:
        mn = min(sm, mn)
        mx = max(sm, mx)
        return

    # 하부 재귀 호출 (dfs) : 연산자 개수가 남아있을 때만 가능
    if add > 0:
        dfs(n+1, sm+lst[n], add-1, sub, mul, div)
    if sub > 0:
        dfs(n+1, sm-lst[n], add, sub-1, mul, div)
    if mul > 0:
        dfs(n+1, sm*lst[n], add, sub, mul-1, div)
    if div > 0:
        dfs(n+1, int(sm/lst[n]), add, sub, mul, div-1)

N = int(input())
lst = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

# 함수 호출
mn, mx = int(1e9), int(-1e9)
dfs(1, lst[0], add, sub, mul, div)

print(mx, mn, sep='\n')