# k = 1
# for i in range(10):
#   for j in range(i):
#     print(k)
#     # k=k+1
# k=15
n = int(input("Please Enter the Number: "))
k = 0
for i in range(n):
  k = k+i
m = n+k
for i in range(n):
  for j in range(i+1):
    print(format(m,"<3"),end= " ")
    m = m - 1
  print()


first_name = input("Please Enter Your First Name : ")
last_name = input("Please Enter Your Last Name: ")
print(f"( Hi Robo !!!! My First Name is {first_name} and My Second Name is {last_name} )")
