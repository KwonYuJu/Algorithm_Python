def dfs(n, lst):
    # 종료조건(n에 관련) + 정답 처리
    if n == M:  # M개 선택 (길이가 M인 수열 완성)
        ans.append(lst)
        return

    # 재귀로 하부함수(dfs) 호출
    for j in range(1, N+1):
        if v[j] == 0:   # 선택하지 않은 숫자인 경우 추가
            v[j] = 1
            dfs(n+1, lst+[j])
            v[j] = 0

N, M = map(int, input().split())
ans = []        # 정답 리스트를 저장할 리스트
v = [0]*(N+1)   # 중복 확인

dfs(0, [])      # dfs 초기값
for lst in ans:
    print(*lst)