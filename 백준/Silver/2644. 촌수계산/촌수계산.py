def bfs(s, e):      # s에서 e까지 최소거리(촌수) 찾기
    q = []          # 다음으로 탐색할 노드를 저장할 큐
    v = [0]*(N+1)   # 방문 여부, 촌수 거리 기록

    q.append(s)     # 초기 데이터, 시작점 s 큐에 추가 방문
    v[s] = 1        # 초기 데이터 방문으로 표시, 촌수 1로 설정

    while q:
        c = q.pop(0)        # 현재 탐색할 노드 c 꺼내기
        if c == e:          # 현재 노드가 목적지 e와 같으면 탐색 종료
            return v[e]-1   # 시작점에서의 초기값을 1로 설정했으므로, 실제 촌수는 v[e]-1

        for n in adj[c]:        # 현재 노드 c와 연결된 모든 노드 n에 대해
            if not v[n]:        # 방문되지 않은 노드 n이라면
                q.append(n)     # 큐에 추가하여 다음 탐색 대상으로 설정
                v[n] = v[c]+1   # n의 촌수는 c의 촌수보다 1만큼 큼

    return -1   # 목적지 e에 도달할 수 없을 경우 (친척 관계가 없을 때)

N = int(input())
S, E = map(int, input().split())
M = int(input())
adj = [[] for _ in range(N+1)]  # 양방향 인접리스트
for _ in range(M):
    p, c = map(int, input().split())
    adj[p].append(c)
    adj[c].append(p)

ans = bfs(S, E)
print(ans)