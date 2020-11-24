#Introduction to Classes in Python"
#Classes are object mappers
#A bluprint for standard code that we can use across the board for different instances
#Classes can have data inside of them or functions and behaviors
#Instantiation: is the process of making an instance
#Dunder = double under (double underscore)
#Self references the instance and must be passed into the function inside the class if you want to call it


class Invoice:

    def gretting(self):
        return 'HI there'

#Created an instance of invoice. So python is storing this instance here
inv_one = Invoice()
print(inv_one)

#Second instance where this class is stored
inv_two = Invoice()
print(inv_two.greeting())




