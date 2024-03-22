l1 = [20,30,40,50,70,80]

def sortedlist(l):
  for i in range(1,len(l)):
    if l[i] < l[i-1]:
      return False
  return True
print(sortedlist(l1))

if sortedlist(l1):
  print('Yes')
else:
  print('No')

# Reversed Method List

def revered(l):
  s = 0
  e = len(l)-1
  while s<e:
    l[s],l[e] = l[e],l[s]
    s = s+1
    e = e-1
  return l
l1 = [10,20,30,40,50]
l2 = revered(l1)
print(l2)

