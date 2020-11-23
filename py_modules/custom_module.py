#How to Import a Custom Python Module into Another File
# libs/helper.py file

def greeting(first, last):
    return f'Hi {first} {last}!'

# main.py file
import sys
sys.path.insert(0, './libs')
import create_module

def render():
    print(create_module.greeting('Kristine', 'Hudgens'))


render()