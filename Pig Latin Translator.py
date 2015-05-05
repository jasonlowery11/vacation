# Pig Latin translator. Enter a word and it will translate to Pig Latin.
#Codecademy Python course

original = input("What's your name? ")

if len(original) > 0 and original.isalpha():
    print(original)
else:
    print("empty")
        
