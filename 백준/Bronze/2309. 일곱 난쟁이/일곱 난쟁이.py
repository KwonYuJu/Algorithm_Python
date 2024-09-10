def find_two_dwarf():
    N = 9
    height = sum(lst) - 100
    for i in range(0, N-1):
        for j in range(i+1, N):
            if lst[i]+lst[j] == height:
                return lst[i], lst[j]

lst = [int(input()) for _ in range(9)]
dwarf1, dwarf2 = find_two_dwarf()
for i in sorted(lst):
    if i != dwarf1 and i != dwarf2:
        print(i)