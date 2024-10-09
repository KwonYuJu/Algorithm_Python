def dfs(n, alst, blst):
    global ans
    if n == N:      # 종료 조건: 모든 사람(n)이 팀에 배정된 경우
        if len(alst) == len(blst):  # A팀과 B팀의 인원 수가 같은 경우에만
            asm = bsm = 0
            for i in range(M):
                for j in range(M):
                    asm += arr[alst[i]][alst[j]]    # A팀 능력치 합
                    bsm += arr[blst[i]][blst[j]]    # B팀 능력치 합
            ans = min(ans, abs(asm-bsm))
        return      # n == N인 경우 재귀 종료

    dfs(n+1, alst+[n], blst)    # 현재 사람 n을 A팀에 추가한 후, 다음 사람 처리
    dfs(n+1, alst, blst+[n])    # 현재 사람 n을 B팀에 추가한 후, 다음 사람 처리

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

M = N//2
ans = 100*M*M   # 능력치 차이의 최소값 저장, 충분히 큰 값으로 초기화
dfs(0, [], [])  # 사람 번호 0부터 시작, 초기 상태 두 팀 모두 빈 리스트
print(ans)      # 최소 능력치 차이