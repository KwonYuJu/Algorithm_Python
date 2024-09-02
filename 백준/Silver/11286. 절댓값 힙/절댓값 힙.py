import heapq
import sys

input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x == 0:              # x가 0이라면
        if len(heap) == 0:  # 만약 배열이 비어 있으면
            print(0)        # 0 출력
        else:               # 배열 비어있지 않으면
            print(heapq.heappop(heap)[1])   # 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거
    else:   # x가 0이 아니라면
        heapq.heappush(heap, (abs(x), x))   # 배열에 x 추가