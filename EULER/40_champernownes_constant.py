def num_length(num):
  return len(str(num))

def count_digits(stop, start=1): # start stop inclusive, start <= stop
  if num_length(start) == num_length(stop):
    return (stop - start + 1) * num_length(start)
  next_10_pow = 10 ** num_length(start)
  return count_digits(next_10_pow - 1, start) + count_digits(stop, next_10_pow)

def get_digit(n):
  low = 1; high = 190000
  while high - low > 1:
    mid = (high + low) // 2
    if count_digits(mid) > n:
      high = mid
    else:
      low = mid
  cat = f"{low%10}{high}"
  extra = n - count_digits(low)
  return int(cat[extra])

ans = 1
for i in range(7):
  ans *= get_digit(10**i)
print (ans)
