txt = list(input())
max_ops = int(input())
n = len(txt)

prfx_sums = [[0 for _ in range(n)] for _ in range(26)]

for i in range(n):
    for j in range(26):
        prfx_sums[j][i] = prfx_sums[j][i - 1] + (txt[i] == chr(ord('a') + j))

from itertools import groupby as g
prfx_sums_helper = [[0 for _ in range(n)] for _ in range(26)]
helper_idx = 0
for (k, v) in g(txt):
    prfx_sum_helper_arr = prfx_sums_helper[ord(k) - ord('a')]
    ct = len(list(v))
    for i in range(helper_idx, helper_idx + ct):
        prfx_sum_helper_arr[i] = helper_idx + ct - 1
    helper_idx += ct

def get_x_chars_or_more(start_index, char):
    prfx_sum_arr = prfx_sums[ord(char) - ord('a')]
    l = start_index; r = n
    while (r - l > 1):
        mid = (l + r) // 2
        width = mid - start_index + 1
        needed_ops = width - (prfx_sum_arr[mid] - prfx_sum_arr[start_index] + 1)
        if needed_ops > max_ops:
            r = mid
        else:
            l = mid
    return l

def get_end_idx(start_index, char):
    cand_end_idx = get_x_chars_or_more(start_index, char)
    real_end_idx = prfx_sums_helper[ord(char) - ord('a')][cand_end_idx] or cand_end_idx
    return real_end_idx

ans = 0
for start_idx in range(n):
    c = txt[start_idx]
    end_idx = get_end_idx(start_idx, c)
    tmp_ans = end_idx - start_idx + 1
    ans = max(ans, tmp_ans)

print(ans)

'''
babcbdb
2

== 5

abcdabcd
2

== 3
'''