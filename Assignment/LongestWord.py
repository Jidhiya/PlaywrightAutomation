Sentence = input("Enter the sentence: ")
words = Sentence.split()
longest_word = ""  
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print("The longest word is:", longest_word)