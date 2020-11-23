#Finding a Substring in Python with: Find, Index, and In

#Python Documentaion
#str.find(sub[,start[,end]])
#Return the lowest index in the string where substring sub is found within the slice s[start:end]. Optional arguments >start and end are interpreted as in slice notation. Return -1 if sub is not found

#Note
#The find() method should be used only if you need to know the position of sub. To check if sub is a substring or >not, use the in operator

#str.index(sub[, start[, end]])
#Like find(), but raise ValueError when the substring is not found.

#The Find Method-- returns -1 if it can't find the value or reutns index of where the str is first discovered

#The Index Method --returns an error if it can't find the value

#The In Operator --prints True or False. Preferred method. Only cares about a true or false value. 
#Allows us to simply know if a string contains a substring


sentence = 'The quick brown fox jumped over the lazy dog.'
query = sentence.find('quick')
print(query)
#Returns index it found quick. The index 4.
#The is called a substring. A str inside of another str we are looking for.

#The .index() returns the same exact thing. However, index will throw and error if it can't find the value and index returns a -1.
sentence = 'The quick brown fox jumped over the lazy dog.'

query = sentence.find('oops')
query_two = sentence.index('oops')

print(query)
print(query_two)

query = 'oops' in sentence

print(query)