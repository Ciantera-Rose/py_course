#Introduction to Classes in Python
#Classes are object mappers. They give you the ability to create a blueprint for objects
#Classes can have data, functions, and behavior inside of them

#This example create a basic function

class Invoice:

  def greeting(self):
    return 'Hi there'


inv_one = Invoice()
print(inv_one.greeting())

inv_one = Invoice()
#Two instances with two spots in memeory where this class is stored

#A base case for understanding the syntax. 
#A class. A function inside of the class. Returns a string.
#We need to create an object with the class. 
#The class is called by a process called "Instantiation"
#This takes the blueprint (class). By itself it does nothing.
#We created an instance of invoice and then called the function
#A default argument must be passed into a class, called self. Self references the instance.
#In each case it references each of the objects created. Self must be passed as the first argument 