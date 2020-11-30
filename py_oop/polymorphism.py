#Using Polymorphism to Build an HTML Generator in Python
#Inheritance is generally coupled with Polymorphism. 
#One item can hhave many forms
#ie. In this example we have an HTML classs with sunclasses of methods

class Html:
    def __init__(self, content):
        self.content = content

#Create an abstract function. This will be used for it's properties only and we will call on that
#Subclass will render this method
#This abstract class is something we the user doesn't come into contact with
    def render(self):             
        raise NotImplementedError("Subclass must implement render method")

#This class inherits from the render
class Heading(Html):
    def render(self):
        return f'<h1>{self.content}</h1>'

#This inherits from HTML class and has its own render method
class Div(Html):
    def render(self):
        return f'<div>{self.content}</div>'

#And now we can create our own HTML tags, each rendering the same behavior but with abiliy to override the output
tags = [Div('Some content'), Heading('My Amazing Heading'), Div('Another div')]

#Now iterate through the list
#Grabs the string values, concatenate : and then call the render functions
#The sub classes have the render method so they can have shared behavior
for tag in tags:
    print(str(tag) + ': ' + tag.render())

for tag in tags:
    print(tag.render())    

'''
Polymorphism defines methods in the child class that have the same names
as the methods from the parent class. In inheritance, the child class inherits 
the methods from the parent class. It is also possible to modify a method in a child 
class that it has inherited from the parent class

'''