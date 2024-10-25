def bfs(s, e):
    q = []
    v = [0]*200001  # 0부터 200000도 포함해야하니까

    q.append(s) # 5를 넣었음
    v[s] = 1    # 인덱스 5인칸에 1로 방문표시 & 몇 초인지
                # 지금은 0초인데 1로하고 나중에 1빼주면 됨

    while q:
        c = q.pop(0)    # 현재위치 q에서 꺼내
        # 종료 조건
        if c == e:      # 현재위치가 끝점에 도달하면 도착
            return v[e]-1   # 0초 때 1로 해둬서 1 빼줘야함

        # 다음 방향, 범위내, 미방문인지 확인
        # 현재위치 c에 대해서 다음에 갈 수 있는 n 판단해보기 
        for n in (c-1, c+1, c*2):
            if 0<=n<=100000 and v[n]==0:
                q.append(n)      # 조건 만족하면 큐에 다음 탐색할 좌표로 추가하고
                v[n] = v[c]+1    # 방문 표시하는데 현재 위치+1 해줘야 몇초인지 알 수 있음
    return -1

N, K = map(int, input().split())

ans = bfs(N, K)
print(ans)