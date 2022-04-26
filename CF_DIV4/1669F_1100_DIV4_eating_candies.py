from collections import deque

for _ in xrange(input()):
    n = input()
    nums = deque(map(int, raw_input().split()))
    alice_ct = 0; bob_ct = 0
    alice_score = 0; bob_score = 0
    ans = 0
    while nums:
        if alice_score < bob_score:
            alice_ct += 1
            alice_score += nums.popleft()
        else:
            bob_ct += 1
            bob_score += nums.pop()
        if alice_score == bob_score:
            ans = alice_ct + bob_ct
    print ans
