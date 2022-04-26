# lpad to 31 bits (2**31 - 1 mx)
for _ in xrange(input()):
    n, k = map(int, raw_input().split())
    nums = map(int, raw_input().split())
    freq = [0] * 31; ans = 0  # idx 0 - 30
    for num in nums:
        for idx in range(31):  # R-L
            cmpl = 30 - idx
            freq[cmpl] += bool(2**idx & num)

    for idx in range(31):
        cmpl = 30 - idx
        if k >= (n - freq[idx]):
            k -= (n - freq[idx])
        else:
            continue
        ans += 2**cmpl
    print ans
