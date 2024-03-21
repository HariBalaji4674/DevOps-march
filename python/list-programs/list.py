from audioop import avg
from unittest import FunctionTestCase


list = [0]

l1 = [10,21,30,40,50]
l2 = ['geeks','for','geeks','is','best']


# Average Function

def average(l):
  sum = 0
  for i in l:
    sum = sum + i
  n = len(l)
  return sum/n

print(average(l1))

# Average using Build in Functions sum and length
sum1 = sum(l1)
n = len(l1)
print(sum1/n)

# Separate Even and odd Values

def evenodd(l):
  even = []
  odd = []
  for i in l:
    if i%2 == 0:
      even.append(i)
    else:
      odd.append(i)
  return even,odd

even,odd = evenodd(l1)
print(even)
print(odd)
# print(evenodd(l1))

# Comprehension Method of Even and odd

def evenodd(l):
  even = [x for x in l if x%2 == 0]
  odd = [x for x in l if x%2 != 0]
  return even,odd

even,odd = evenodd(l1)
print(even)
print(odd)

# Print all Vowels in a string
st = "harivardhanreddy"
strList = []
for i in st:
  if i in 'aeiou':
    strList.append(i)
    # print(i)
print(strList)


# Slicing In a Python Function list[start:stop:increment/step]
for i in l1[1:3]:
  print(i)

# Convert List to Dictionary
dict1 = dict(zip(l1,l2))
print(dict1)

# Inverted Dictionary
d1 = {v:k for (k,v) in dict1.items()}
print(d1)


# Power for each number in list convert them into mapping elements like dictionary

d1 = {i:i**2 for i in l1 if i%2 == 0}
print(d1)


# Largest Element in the list

def largest(l):
  if not l:
    return None
  else:
    res = l[0]
    for i in range(1,len(l)):
      if l[i]>res :
        res = l[i]
    return res

# l2 = []
print(largest(l1))

# List to dictionary
dict1 = { x:y for (x,y) in (l1,l2) }
print(dict1)

