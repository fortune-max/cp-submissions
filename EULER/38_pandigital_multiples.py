from itertools import permutations

def calc_pandigital(n: int):
  ans, multiplier = "", 0
  while len(ans) < 9:
    multiplier += 1
    ans += str(n * multiplier)
    if len(ans) >= 9:
      return ans if sorted(ans) == sorted("123456789") else 0

def is_achievable(pandigital: str):
  for n_width in range(1, 5):
    seed = int(pandigital[:n_width])
    if calc_pandigital(seed) == pandigital:
      return True
  return False

for pandigital_candidate in permutations("987654321"):
  pandigital_candidate = "".join(pandigital_candidate)
  if is_achievable(pandigital_candidate):
    print(pandigital_candidate)
    break
