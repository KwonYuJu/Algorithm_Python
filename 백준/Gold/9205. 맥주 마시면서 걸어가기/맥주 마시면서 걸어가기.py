def bfs(sj, si, ej, ei):
    q = []      # 큐 생성
    v = [0]*N   # v배열 생성

    q.append((sj, si))  # 큐에 처음 탐색할 좌표 append, v배열에는 표시 안함 (편의점만 방문 표시)

    while q:
        cj, ci = q.pop(0)   # 현재 탐색할 좌표 꺼내기
        if abs(cj-ej)+abs(ci-ei) <= 1000:   # 현재좌표랑 도착점 좌표랑 거리가 1000이내이면 목적지 도달 가능
            return 'happy'

        for i in range(N):  # 미방문, 범위내인지 확인
            if v[i] == 0:   # 미방문이면
                nj, ni = lst[i]     # 다음에 갈 수 있는 좌표이므로 꺼낸다
                if abs(cj-nj)+abs(ci-ni) <= 1000:   # 현재좌표랑 다음좌표랑 거리가 1000이내 이면
                    q.append((nj, ni))  # 다음 탐색할 편의점으로 큐에 추가
                    v[i] = 1    # 현재 좌표는 방문으로 표시
    return 'sad'

TC = int(input())       # 테스트케이스 개수
for _ in range(TC):
    N = int(input())    # 편의점 개수
    sj, si = map(int, input().split())  # 출발점
    lst = []    # 편의점 좌표 담을 리스트
    for _ in range(N):
        pj, pi = map(int, input().split())  # 편의점 좌표
        lst.append((pj, pi))    # 편의점 좌표 bfs 하기 위해 리스트에 append
    ej, ei = map(int, input().split())  # 도착점

    ans = bfs(sj, si, ej, ei)
    print(ans)