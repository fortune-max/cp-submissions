from collections import defaultdict as d

for _ in xrange(input()):
    n = input()
    ans = 0
    freq_1 = d(int); freq_2 = d(int); freq_12 = d(int)
    for t in xrange(n):
        txt = raw_input()
        fl, sl = txt[0], txt[1]
        ans += freq_1[fl] + freq_2[sl] - 2*freq_12[txt]
        freq_1[fl] += 1; freq_2[sl] += 1; freq_12[txt] += 1
    print(ans)
