from itertools import groupby as g
from collections import defaultdict as d


def process():
    # get starter
    for idx, txt in enumerate(txts):
        f_c = txt[0]
        if idx not in not_taken:
            continue
        is_same = len(set(txt)) == 1; is_not_same = not is_same
        if len(enders[f_c] - sames[f_c]) == 0 and len(starters[f_c] - sames[f_c]) <= 1 and ((is_same and idx in sames[f_c]) or (is_not_same and not sames[f_c])):
            to_start, ans = idx, txt
            not_taken.remove(idx)
            break
    else:
        return "", 0

    while not_taken:
        # first fulfill sames
        for sub_idx in (sames[ans[-1]] & not_taken):
            ans += txts[sub_idx]
            not_taken.remove(sub_idx)
        # check if starters are one if not break
        start_cands = (starters[ans[-1]] & not_taken)
        if len(start_cands) > 1:
            return "", 0
        elif len(start_cands) == 0:
            return ans, True
        sub_idx = start_cands.pop()
        ans += txts[sub_idx]
        not_taken.remove(sub_idx)

    return ans, False


def test(my_txt):
    arr = []
    for k, v in g(my_txt):
        arr.append(k)
    return len(arr) == len(set(arr))


for T in range(1, 1+int(input())):
    n = int(input())
    txts = input().split()
    starters, enders, sames, not_taken = d(set), d(set), d(set), set(range(n))
    for idx, txt in enumerate(txts):
        if len(set(txt)) == 1:
            sames[txt[0]].add(idx)
        starters[txt[0]].add(idx)
        enders[txt[-1]].add(idx)

    cont, ans = True, ""
    while not_taken and cont:
        ans_tmp, cont = process()
        ans += ans_tmp

    if not_taken and not cont:
        print(f"Case #{T}: IMPOSSIBLE")
    else:
        if test(ans):
            print(f"Case #{T}: {ans}")
        else:
            print(f"Case #{T}: IMPOSSIBLE")
