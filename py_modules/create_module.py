#How to Create a Custom Module and Import It In the Python Repl
#Import core library inside repl and press enter

import math

math.sqrt(4)

# Place in file create_module.py
def greeting(first, last):
  return f'Hi {first} {last}!'

  print(greeting('Kristine', 'Hudgens'))

# Call from repl
import create_module

create_module.greeting('Kristine', 'Hudgens')