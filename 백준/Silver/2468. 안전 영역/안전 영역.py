from collections import deque

def bfs(si, sj, h):
    q = deque()
    # 초기 데이터 준비
    q.append((si, sj))  # 첫 탐색할 좌표
    v[si][sj] = 1       # 방문으로 표시

    while q:
        ci, cj = q.popleft()    # 현재 탐색할 좌표 꺼내
        # 4방향, 범위내, 미방문, + 높이>h
        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
            ni, nj = ci+di, cj+dj   # 다음 인접 좌표 구해서 조건 맞는지 확인
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]>h:
                q.append((ni,nj))   # 조건 맞으면 다음에 탐색하기 위해 q에 추가
                v[ni][nj] = 1       # 방문으로 표시

def solve(h):
    cnt = 0     # h 높이에 대해 잠기지 않는 영역 개수 카운트
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0 and arr[i][j] > h:  # 아직 방문하지 않았고 물에 잠기지 않을 때
                bfs(i, j, h)    # bfs 탐색
                cnt += 1        # 영역 개수 1 증가
    return cnt

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for h in range(100):    # 모든 물의 높이에 대해서 계산해봐야해서
    v = [[0]*N for _ in range(N)]   # 각 높이마다 v배열 초기화
    ans = max(ans, solve(h))        # 높이마다 최대값 갱신
print(ans)