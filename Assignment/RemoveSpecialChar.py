Str = input("Enter a string: ")
special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~\\"
cleaned_str = ""    
for char in Str:
    if char not in special_chars:
        cleaned_str += char 
print("String after removing special characters:", cleaned_str)