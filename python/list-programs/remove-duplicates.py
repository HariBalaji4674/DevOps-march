# string = input("Please Enter the string: ")
# print(string)

string = "peddireddyharivardhanreddy"
dup_string = ""
for i in string:
  if i not in dup_string:
    dup_string = dup_string+i
print(dup_string)


