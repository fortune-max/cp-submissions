n = int(input())
nums = list(map(int, input().split()))
ct = 0
for i in range(1, n-1):
    if (nums[i-1] > nums[i]) and (nums[i+1] > nums[i]):
        ct += 1
print(ct)
