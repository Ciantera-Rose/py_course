#How to Import a Single Function from a Python Module
#To use a function in the from another file, tell Python to look in the file you want
#and then import the function you want to use in the current file.

from math import sqrt
from create_module import greeting

sqrt(4)

import sys
sys.path.insert(0, './libs')

def render():
    print(greeting('Tiffany', 'Hudgens'))


render()

