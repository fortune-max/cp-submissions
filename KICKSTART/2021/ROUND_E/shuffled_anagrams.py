from collections import defaultdict as d


def prob(txt):
    len_, sort_txt = len(txt), sorted(txt)
    dic, ans = d(list), [0] * len_
    enum_txt = list(enumerate(txt))
    for idx, char in enumerate(txt):
        dic[char].append(idx)
    if [1 for v in dic.values() if len(v) > len_ / 2]:
        return "IMPOSSIBLE"
    for _ in range(len_):
        nxt = sorted(sort_txt, key=lambda x: sum([len(dic[k]) for k in (set(dic) - set(x))]))[0]
        for idx, char in enum_txt:
            if char == nxt:
                enum_txt[idx] = (idx, "")
                break
        opt = sorted(set(dic) - set(char), key=lambda x: len(dic[x]))[-1]
        ans[idx] = opt
        dic[opt].pop()
        sort_txt.pop(sort_txt.index(nxt))
    return "".join(ans)


def test_impossible(times=10):
    import tester
    count = 0
    while count <= times:
        txt = tester.gen_rand_arr(str, tester.randrange(1, 10))
        scrambled_txt = tester.scramble_string(txt)
        if not [1 for (a, b) in zip(txt, scrambled_txt) if a == b]:
            count += 1
            if prob(txt) == "IMPOSSIBLE":
                print(txt, prob(txt), "FAILED")


def test_possible(times=10):
    import tester
    for _ in range(times):
        txt = tester.gen_rand_arr(str, tester.randrange(1, 10))
        ans = prob(txt)
        if [1 for (a, b) in zip(txt, ans) if a == b]:
            print(txt, prob(txt), "FAILED")


for i in range(int(input())):
    print(f"Case #{i+1}: {prob(input())}")
