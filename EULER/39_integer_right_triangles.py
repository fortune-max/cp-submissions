freqs = [0 for _ in range(1001)]
ans_freq, ans_val = 0, 0

for p in range(12, 1001):
  for a in range(3, 334):
    for c in range(a+1, p-2*a+1):
      b_exp_sq = (p - a - c) ** 2
      real_b_sq = c**2 - a**2
      if b_exp_sq == real_b_sq:
        freqs[p] += 1
        if freqs[p] > ans_freq:
          ans_freq, ans_val = freqs[p], p

print(ans_val)
