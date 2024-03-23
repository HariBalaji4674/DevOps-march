list = ['a','b','c','d','e','g','h','i']
print(list)

# list = list[1:]+list[0:1]
# print(list)
list = list[-len(list):]
print(list)
# list[start,stop,increment]

list = list[0:len(list):2]
print(list)

#Swapping The elements
a,b = 20,30
a,b = b,a
print(a,b)

# Swapping elements in a List
def swappingPositions(list,position1,position2):
  list[position1],list[position2] = list[position2],list[position1]
  return list

list = [10,20,30,40]
position1 = 1
position2 = 3

print(swappingPositions(list,position1,position2))



