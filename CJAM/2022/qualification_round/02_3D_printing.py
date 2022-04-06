T = int(input())
for t in range(1, T+1):
    p_1 = list(map(int, input().split()))
    p_2 = list(map(int, input().split()))
    p_3 = list(map(int, input().split()))
    arr = []
    for i in range(4):
        arr.append(min([x[i] for x in [p_1, p_2, p_3]]))
    if sum(arr) < 1e6:
        ans = "IMPOSSIBLE"
    else:
        ans = []
        taken = 0
        for i in range(4):
            nxt = arr.pop()
            to_take = min(1000000 - taken, nxt)
            taken += to_take
            ans.append(to_take)
        ans = " ".join(map(str, ans[::-1]))
    print("Case #%d: %s" % (t, ans))
