#Building Polymorphic Functions in Python
#Ability to the function a different behavior

class Heading:
    def __init__(self, content):
      self.content = content

    def render(self):
      return f'<h1>{self.content}</h1>'

class Div:
  def __init__(self, content):
    self.content = content

  def render(self):
    return f'<div>{self.content}</div>'

#In this example we store each one on their own variables
div_one = Div('Some content')
heading = Heading('My Amazing Heading')
div_two = Div('Another div')

#This render takes a tag object, and takes anything that has a render function
#Instead of having an abstract class we were able to use the render function
#If you have quite a bit of shared behavior then use Inheritance

def html_render(tag_object):
  print(tag_object.render())

html_render(div_one)
html_render(div_two)
html_render(heading)

#Concepts to grasp

#Parent Class

class Fish:
    def __init__(self, first_name, last_name)