from collections import deque

for T in range(1, 1+int(input())):
    n, ans, mx = int(input()), 0, -1
    nums = deque(map(int, input().split()))
    while nums:
        take = nums.popleft() if nums[0] < nums[-1] else nums.pop()
        ans += take >= mx
        mx = max(mx, take)
    print(f"Case #{T}: {ans}")
