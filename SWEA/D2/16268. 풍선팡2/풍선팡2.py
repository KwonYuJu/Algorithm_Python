def balloon(y,x):
    direction = [(-1,0),(1,0),(0,-1),(0,1)]
    sum_v = arr[y][x]
    for dy,dx in direction:
            ny,nx = y+dy, x+dx
            if 0<=ny<N and 0<=nx<M:
                sum_v += arr[ny][nx]
    return sum_v

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = max(balloon(i,j) for i in range(N) for j in range(M))
    print(f'#{tc} {result}')