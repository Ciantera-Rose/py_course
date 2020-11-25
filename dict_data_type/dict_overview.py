#Overview of Python Dictionaries
#Syntax for dictionaries in Python is to use curly brackets {...}

#Dictionaries contain key value pairs
#In this exaample the keys are the positions and the values are the players
#To query information in a dictionary you use the key;value pairs to grab the data you want to retrieve 
#The items in the dictionary are case sensitive.

players = {
  "ss": "Correa",
  "2b": "Altuve",
  "3b": "Bregman",
  "DH": "Gattis",
  "OF": "Springer",
}

second_base = players['2b'] #Calls the value pair "Altuve"
designated_hitter = players['DH'] #Calls the value pair "Grattis"

print(designated_hitter)