N = int(input())
lst = [0]*1001
mx_i = mx = 0
for _ in range(N):
    L, H = map(int, input().split())
    lst[L] = H
    if mx < H:      # 최대 높이 값이 높이 H보다 작으면
        mx = H      # H로 최대 높이 값 갱신
        mx_i = L    # L로 최대 좌표값 갱신

# 왼쪽부터 mx_i(포함)까지/ 최대 높이 기준 왼쪽 넓이
ans = mx = 0
for i in range(0, mx_i+1):
    mx = max(mx, lst[i])
    ans += mx

# 오른쪽에서 mx_i 전까지/ 최대 높이 기준 오른쪽 넓이
mx = 0
for i in range(1000, mx_i, -1):
    mx = max(mx, lst[i])
    ans += mx

print(ans)