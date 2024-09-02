from collections import deque

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited_dfs = [0] * (n+1)
visited_bfs = [0] * (n+1)

# dfs
def dfs(v):
    visited_dfs[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if not visited_dfs[i] and graph[v][i] == 1:
            dfs(i)

# bfs
def bfs(v):
    q = deque([v])
    visited_bfs[v] = 1
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if not visited_bfs[i] and graph[v][i] == 1:
                q.append(i)
                visited_bfs[i] = 1

dfs(v)
print()
bfs(v)