def dfs(i):
    global ans
    # [1] 종료조건
    if i == N:      # i는 행 번호 / N행까지 진행한 경우 : 성공
        ans += 1    # 경우의 수 +1
        return      # 종료

    # [2] 하부호출 dfs
    for j in range(N):  # 열 순회 (0부터 N-1까지)
        if v1[j]==v2[i+j]==v3[i-j]==0:  # 열,대각선 아직 퀸 없음 (놓을 수 있음)
            v1[j]=v2[i+j]=v3[i-j]=1     # 방문 표시
            dfs(i+1)
            v1[j]=v2[i+j]=v3[i-j]=0     # 방문 해제

N = int(input())
ans = 0         # 퀸을 놓는 경우의 수
v1 = [0]*N      # 열 체크
v2 = [0]*(2*N)  # i+j 대각선 체크
v3 = [0]*(2*N)  # i-j 대각선 체크
dfs(0)
print(ans)