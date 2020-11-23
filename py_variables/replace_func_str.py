#Using Python's replace Function to Find and Replace String Values

sentence = 'The quick brown fox jumped over the lazy dog.'

sentence = sentence.replace('quick', 'slow')

print(sentence.replace('quick', 'slow'))
print(sentence)

#returns "The slow brown fox jumped over the lazy dog"
#String are immutable objects so we aren't changing the original string
#We can leverage the replace() function with a reassignemt process to change the string. 
#So we can use the same vairble name and reassign it or creare a new vairable name to preform what we want to change in that instance.
