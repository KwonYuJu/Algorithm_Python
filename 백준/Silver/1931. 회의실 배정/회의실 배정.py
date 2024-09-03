N = int(input())
meeting = []
for i in range(N):
    start, end = map(int, input().split())
    meeting.append((start, end))
meeting.sort(key = lambda x: (x[1], x[0]))
end_time = 0
cnt = 0
for start, end in meeting:
    if start >= end_time:
        end_time = end
        cnt += 1
print(cnt)
