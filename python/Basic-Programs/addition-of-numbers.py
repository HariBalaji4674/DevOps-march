from numpy import add
'''
number = int(input("Please Enter The Number : "))
sum = 0
for i in range(number+1):
  sum = sum + i
print(sum)
'''
# Addition of Two Numbers using inbuild function
n1 = 100
n2 = 200
n3 = add(n1,n2)
print(f"(The sum of two numbers are {n3} )")
print(format(n3,"<3"))
print(f"The sum of {n1} and {n2} is {n3}".format(n1,n2,n3))

# Numbers
numbers = dict()
print(numbers)

numbers = {1:'one',2:'two',3:'Three'}
print(numbers)

del numbers[3]
print(numbers)

print(1 in numbers,2 in numbers,3 in numbers)

# Reverse the array
list = [1,2,3,4,5]
rev_list = list[::-1]  # [Start:End:Increment/Decrement/Step]
print(rev_list)

# 7008629229

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
list3 = list1 + list2
print(list3)
