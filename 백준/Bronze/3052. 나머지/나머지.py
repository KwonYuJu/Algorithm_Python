nums = []
for i in range(10):
    N = int(input())
    if N % 42 not in nums:
        nums.append(N % 42)
print(len(nums))