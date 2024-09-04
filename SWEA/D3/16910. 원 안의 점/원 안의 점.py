def count_point(N):
    count = 0
    for x in range(-N, N+1):
        for y in range(-N, N+1):
            if x**2 + y**2 <= N**2:
                count += 1
    return count

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = count_point(N)
    print(f"#{tc} {result}")