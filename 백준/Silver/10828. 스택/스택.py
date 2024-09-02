N = int(input())

stack = []

for _ in range(N):
    order = input()

    if 'push' in order:
        push_num = int(order[5:])
        stack.append(push_num)
    if order == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    if order == 'size':
        print(len(stack))
    if order == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    if order == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
