from itertools import groupby as g
n = input()
txt = raw_input()
ans = 0
for k, v in g(txt):
    ans += 1

print ans - (txt[-1] == '0')
