next_digits = [1, 3, 5, 7, 9]
real_truncatable_primes = []

def is_prime(n):
  if n < 2:
    return False
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      return False
  return True

def is_truncatable_prime(n):
  if n < 10:
    return False
  for i in range(1, len(str(n))):
    if not is_prime(n % 10**i):
      return False
    if not is_prime(n // 10**i):
      return False
  return True

def get_next(root, next_digit):
  candidate = root * 10 + next_digit
  if is_prime(candidate):
    if is_truncatable_prime(candidate):
      real_truncatable_primes.append(candidate)
    for digit in next_digits:
      get_next(candidate, digit)

for root in [2, 3, 5, 7]:
  for next_digit in next_digits:
    get_next(root, next_digit)
print(sum(real_truncatable_primes))
