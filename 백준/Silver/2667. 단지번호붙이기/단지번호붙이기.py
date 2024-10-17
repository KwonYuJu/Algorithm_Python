def bfs(si, sj):
    q = []  # 앞으로 탐색해야 할 좌표를 큐에 append할 것임
    q.append((si,sj))   # 초기 시작 좌표
    v[si][sj] = 1       # 해당 좌표는 방문으로 표시
    cnt = 1             # 아파트 개수 초기값 1

    # 큐에 탐색해야 할 좌표가 남아 있는 동안(더 이상 탐색할 좌표가 없을 때까지)
    while q:
        ci, cj = q.pop(0)   # 현재 탐색할 좌표 꺼냄
        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)): # 현재 좌표 기준 4방향 탐색
            ni, nj = ci+di, cj+dj   # 현재 좌표에서 4방향으로 이동한 새로운 좌표 (ni, nj)
            # 만약 ni, nj가 범위 벗어나지 않고, 방문하지 않았고, 아파트가 있으면
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]==1:
                q.append((ni, nj))  # q에 다음에 탐색할 대상으로 추가
                v[ni][nj] = 1       # 방문 처리, 이후에 다시 탐색하지 않도록
                cnt += 1            # 아파트 개수 증가
    return cnt  # 아파트 단지의 아파트 개수 반환

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

v = [[0]*N for _ in range(N)]
ans = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and v[i][j] == 0: # 아파트이고, 방문하지 않은 경우
            ans.append(bfs(i,j))    # bfs를 호출하여 연결된 아파트 개수 반환

ans.sort()
print(len(ans), *ans, sep='\n')