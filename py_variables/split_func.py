#Guide to the Python split Function
#Split takes in an argument of where you want to split your string
#Returns a list vs partition which returns a tuple

tags = 'python,coding,programming,development'

list_of_tags = tags.split(',')
#returns ['python','coding','programming','development']
#splits into 4 separate elements at the ',' within a list
list_of_tags = tags.split()
#Returns ['python,coding,programming,development']
#By default if you don't pass in any arguments in puts the string in a list

print(list_of_tags)

heading = "Python: An Introduction"

heading, subheading = heading.split(': ')

print(heading)
print(subheading)
#Returns ["Python, An Introduction"]
#In this case Partition would be a better use