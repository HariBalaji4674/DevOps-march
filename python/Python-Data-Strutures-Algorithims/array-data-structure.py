from typing import Counter


arr = [1,2,3,4,5,'a','b','c']

for i in arr:
  print(id(i))
# print(id(arr))

arr.append(10)
print(arr)

arr.insert(4,14)
print(arr)

arr.insert(3,'d')
print(arr)

numbers1 = [1,2,3]
numbers2 = [4,5,6]
numbers1.extend(numbers2)
print(numbers1)

arr = {1,2,3,4,5}
print(arr)

def _sum(arr):
  sum = 0
  for i in arr:
    sum = sum + i
  return sum
if __name__ == "__main__":
  arr = [1,2,3,4,5]
  n = len(arr)
  ans = _sum(arr)
  print(f"Sum of An Arrays are {ans}")

numbers1 = [2,6,8,9,10]
summing  = sum(numbers1)
print(summing)


# Counter method Used to count the occurences of elements in an array it is from collections methods

arr = [12,13,4,5,23,22,22]
c = Counter(arr)
print(c)
sum = 0
for keys,values in c.items():
  sum = sum + keys*values
  # print(keys,values)
print(sum)

