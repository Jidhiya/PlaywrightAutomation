Str = input("Enter a string: ")
vowels = []
consonants = []
for char in Str:
    if char.isalpha():
        if char.lower() in 'aeiou':
            vowels.append(char)
        else:
            consonants.append(char)

print("Vowels:", ' '.join(vowels))
print("Count of Vowels:", len(vowels))
print("Consonants:", ' '.join(consonants))
print("Count of Consonants:", len(consonants))