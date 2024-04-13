# Greatest Common Divisors or Highest Common Factors

def gcd(a,b):
  if a == 0:
    return b
  return gcd(b%a,a)

print(gcd(36,60))

def gcd(a,b):
  if a == 0:
    return b
  return gcd(b%a,a)

print(gcd(60,36))

def gcd(a,b):
  if a == 0:
    return b
  return gcd(b%a,a)

print(gcd(60,36))