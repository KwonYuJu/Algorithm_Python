# dr : 북0 동1 남2 서3
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
def solve(ci, cj, dr):
    cnt = 0     # 청소한 공간 수
    # 청소기가 더 이상 움직일 곳이 없고, 후진을 시도했는데 벽을 만나 더 이상 움직일 수 없을 때 종료
    while 1:
        # 1. 현재 위치 청소
        arr[ci][cj] = 2
        cnt += 1

        # 2. 왼쪽 방향으로 순서대로 탐색해서 미청소 구역이 있으면 이동&방향설정, 없으면 후진
        flag = 1    # 미청소 구역을 찾으면 flag = 0으로 설정되고, 그 위치로 청소기 이동 -> while 1: 루프 다시 시작
        while flag == 1:    # flag == 1인 동안 네 방향 탐색하여 미청소 구역을 찾을 때까지 반복
            # 왼쪽부터 네 방향 중 미청소 영역 있는 경우
            for nd in ((dr+3)%4, (dr+2)%4, (dr+1)%4, dr):
                ni, nj = ci+di[nd], cj+dj[nd]
                if arr[ni][nj] == 0:    # 미청소 영역 찾으면
                    ci, cj, dr = ni, nj, nd # 청소기를 미청소 영역으로 이동시키고, 방향도 바꿈
                    flag = 0    # 미청소 영역 찾았으니까 탐색 종료
                    break       # 네 방향 탐색 루프에서 빠져나감
            else:   # 4방향 모두 미청소 영역 없으면 -> 후진
                bi, bj = ci-di[dr], cj-dj[dr]   # 현재 방향으로 후진할 위치 계산
                if arr[bi][bj] == 1:  # 후진할 위치가 벽이면 청소 종료
                    return cnt  # 청소 완료한 칸 수 반환
                else:   # 벽이 아니면 후진
                    ci, cj = bi, bj # 후진한 새로운 위치로 이동

    # 이론적으로 도달하지 않음 (오류 방지를 위한 안전장치)
    return -1

N, M = map(int, input().split())
si, sj, dr = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = solve(si, sj, dr)
print(ans)