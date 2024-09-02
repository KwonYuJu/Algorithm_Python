def fly(y, x, N, M, arr):
    direction1 = [(-1,0),(1,0),(0,-1),(0,1)]    # + 방향
    direction2 = [(-1,-1),(-1,1),(1,-1),(1,1)]  # x 방향

    # + 방향
    sum_v1 = arr[y][x]
    for dy,dx in direction1:
        for m in range(1, M):   # M 범위 중요
            ny = y+dy*m
            nx = x+dx*m
            if 0<=ny<N and 0<=nx<N:
                sum_v1 += arr[ny][nx]

    # x 방향
    sum_v2 = arr[y][x]
    for dy,dx in direction2:
        for m in range(1, M):   # M 범위 중요
            ny = y+dy*m
            nx = x+dx*m
            if 0<=ny<N and 0<=nx<N:
                sum_v2 += arr[ny][nx]

    return max(sum_v1, sum_v2)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = max(fly(i, j, N, M, arr) for i in range(N) for j in range(N))
    print(f'#{tc} {result}')