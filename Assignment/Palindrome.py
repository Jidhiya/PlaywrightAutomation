str_1 = input("Enter the string: ")
str_2 = ""
for char in str_1:
    str_2 = char + str_2
print(str_2)
if str_1 == str_2:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

    


