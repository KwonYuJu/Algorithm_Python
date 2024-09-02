import sys
input = sys.stdin.readline
N = int(input())

queue = []

for _ in range(N):
    order = input().strip()

    if 'push' in order:
        push_num = int(order[5:])
        queue.append(push_num)
    if order == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    if order == 'size':
        print(len(queue))
    if order == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    if order == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    if order == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)

