arr = [list(input()) for _ in range(5)]
arr_t = list(zip(*arr))
result = []

max_len = max(len(row) for row in arr)

for i in range(max_len):
    for row in arr:
        if i < len(row):
            result.append(row[i])
print(''.join(result))