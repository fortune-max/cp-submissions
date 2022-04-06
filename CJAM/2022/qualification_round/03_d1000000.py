T = int(input())
for t in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort(reverse = True)
    idx = 1
    while nums:
        pop = nums.pop()
        if pop >= idx:
            idx += 1
    print("Case #%d: %s" % (t, idx-1))
