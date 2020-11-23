#How to Check if Strings Represent Numbers or Alphanumeric Characters in Python
#Side note: So what is API data?
#Application Programming Interface
#A set of functions and procedures allowing the creation of applciations that access the features
#or data of an operating system, application, or other services
#So this guide covers how you can check fo rin, inner data w/ API responses
#Most API data comes in a string format


api_data = '5'
#API data variable that is a string that contains an int
greeting = 'Hi there'

print(api_data.isalpha())
#returns False

print(greeting.isalpha())
#returns True

print(api_data.isnumeric())
#returns True
#Is the value numeric, yes, a int inside a str
print(greeting.isnumeric())
#returns False
#Not a number, so returns false

#Isalpha may give some false positives because spaces will be counted as an index and is counted as numeric
#due to thhe zero based numbering system