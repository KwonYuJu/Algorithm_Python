num = [int(input()) for _ in range(9)]
max_num = max(num)
max_idx = num.index(max_num)
print(max_num)
print(max_idx+1)