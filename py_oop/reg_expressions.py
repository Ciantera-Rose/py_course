#Using Regular Expressions to List File Types in Python
#Simple use case to find the file types
#Regular expressions give you the ability to match patterns

import fnmatch #Built into Python
from fnmatch import fnmatchcase #Allows access to the operating system 
import os


#In a real world application you could grab files from the file system that are a certain file type and perfrom processes on them

#Create file we want to add Python code to

def list_files():
    for file in os.listdir('.'): #'.' to access same directory you are in. Loop over files and do some action with them
        if fnmatch.fnmatch(file, '*.txt'): #Calling the module library and the function. Pass in string argument
            print('Text files:', file) 

        if fnmatch.fnmatch(file, '*.rb'): #While in loop, ypu can preform any other conditions you'd would like
            print('Ruby files:', file)

        if fnmatch.fnmatch(file, '*.yml'):
            print('Yaml files:', file)

        if fnmatch.fnmatch(file, '*.py'):
            print('Python files:', file)


list_files()

players = [
    "Jose Altuve 2B",
    "Carlos Correa SS",
    "Alex Bregman 3B",
    "Scooter Gennett 2B"
]

#Filter players array
#Loops through player list and grabs player items
#Creates a whole other list as it loops through
#Pass in player and position
#Calling fnmatchhcase. 
#Allows to find patterns in the data
second_base_players = [player for player in players if fnmatchcase(player, "* 2B")]

print(second_base_players)

