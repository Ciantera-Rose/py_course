#You may access values inside of strings
#Each element of the string as index
#Python uses a zero based numbering system
#The index of the first element hhas an index of 0

# The quick brown fox jumped
# T => 0
# h => 1
# e => 2
# ' ' => 3


#index = 26

starter_sentence = 'The quick brown fox jumped'

#When working with ranges the range prints up to but not including the last number stated.
first_word = starter_sentence[0:2]

new_sentence = 'Thy' + starter_sentence[3:]

print(new_sentence)

#Prints: Thy quick brown fox jumped
#Adds the string to the sentence from the index of 3: (colon means to everything else if no number comes after it.
