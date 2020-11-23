#You may change and manipulate the case of a string
#You may use this for the ability to call functions and methods on objects

# sentence = 'The quick brown fox jumped'
# sentence -> variable
# 'The quick brown fox jumped' -> string
# = -> assignment

#May call function on sentence or print statement
#If you call a function on thhe object in the varibale it's assigned to it will be tha way everytime it's called
#If you call it in the print statement it will only be called in that instance
#Strings are mutable objects, meaning they can be changed

#Converts entire sentence to uppercase
sentence = 'The quick brown fox jumped'
sentence_two = sentence.upper()

print(sentence)
print(sentence_two)

#Converts first letter of first word in sentence to a capital letter
sentence = 'the quick brown fox jumped'.capitalize()
print(sentence)

#Converts first letter of every word in sentence to a capital letter
sentence = 'the quick brown fox jumped'.title()
print(sentence)

#Converts every letter of every word to lowercase
sentence = 'THE QUICK BROWN FOX JUMPED'
print(sentence.lower())