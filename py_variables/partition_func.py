#Guide to Python's Partition Function
#Breaks string into 3 components
#Main heading : subheading

#3 variables in a row
#Partition takes an argumemnt, the divider
#It's going to look inside the string for whatever you pass in as the argument. In this case the : and the space. 
#Once it finds that it partions the enitre string and separates it into 3 elements
#Python 1st element ... : the 2nd element ... An Introduction the 3rd element
#Whenever you call partition, it returns a tuple collection. 
#Performs variable deconstruction
# the _ represents values you do not want to use

heading = "Python: An Introduction"

header, _, subheader = heading.partition(': ')

print(header) #returns Python
print(subheader) #returns An Introduction

first, second, third = heading.partition(': ')

print(first)
print(second)
print(third)

heading = "Python: An Introduction, and Python: Advanced"
#In this instance it returns Python, :, and then everything after that. 
#So use is for 3 elements only and it starts at the first :