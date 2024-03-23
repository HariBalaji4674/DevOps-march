ls1 = [10,20,30,40,50]
ls2 = [20,40,50,70,80]
print(ls1,ls2)
# ls1.append(ls2)
# print(ls1)

# Swapping an Element
size = len(ls1)
temp = ls1[0]
ls1[0] = ls1[size-1]
ls1[size - 1] = temp

print(ls1)

def swappingElement(l):
  size = len(l)
  temp = l[0]
  l[0] = l[size-1]
  l[size-1] = temp
  return l
print(swappingElement(ls1))

def swapele(l):
  size = len(l)
  l[0],l[-1] = l[-1],l[0]
  return l
print(swapele(ls1))

list = [1,2,3,4]

a,*b,c = list
print(a,b,c)

def swapOperator(l):
  start,*middle,end = l
  l = [end,*middle,start]
  return l
print(ls1)


list = ['a','b','c','d','e','f','g']
print(list)
first,*middle,end = list
list = [end,*middle,first]
print(list)

