Str = input("Enter a string: ")
for char in set(Str):
    count = Str.count(char)
    print(f"'{char}' occurs {count} time(s) in the string.")