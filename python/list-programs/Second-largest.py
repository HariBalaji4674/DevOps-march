l1 = [10,22,52,46,75]

def getmax(l):
  if len(l) < 1:
    return None
  else:
    res = l[0]
    for i in range(1,len(l)):
      if l[i] > res:
        res = l[i]
    return res
print(getmax(l1))

# Second Method of Max number
def getmax(l):
  res = l[0]
  for i in range(1,len(l)):
    res = max(res,l[i])
  return res
print(getmax(l1))


# Second Largest Number in a list
def getsecmax(l):
  lar = l[0]
  slar = None
  if len(l) < 1:
    return None
  for x in l[1:]:
    if x > lar:
      slar = lar
      lar = x
    elif x != lar:
      if slar == None or slar < x:
        slar = x
  return slar
print(getsecmax(l1))



