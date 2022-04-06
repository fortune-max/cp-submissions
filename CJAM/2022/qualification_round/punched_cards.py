T = input()
for t in range(1, T+1):
    R, C = map(int, raw_input().split())
    top_line = ".." + "+-" * (C-1) + "+"
    second_line = ".." + "|." * (C-1) + "|"
    one = "+" + "-+" * C
    two = "|" + ".|" * C
    last_line = one
    ans = top_line + "\n" + second_line + "\n"
    for c in range(R-1):
        ans += one + "\n" + two + "\n"
    ans += last_line
    print "Case #%d:\n%s" % (t, ans)