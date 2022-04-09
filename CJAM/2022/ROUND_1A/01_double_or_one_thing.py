T = int(input())
for t in range(1, T+1):
    ans = ""
    txt = input()
    for i in range(len(txt)):
        if txt[:i] + txt[i] + txt[i:] < txt:
            ans += txt[i] * 2
        else:
            ans += txt[i]
    print("Case #" + str(t) + ": " + ans)
