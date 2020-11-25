#Guide to Python Dictionary View Objects
#View objects allow us to peak in and view all of the items inside of dictionaries
#Provides a dynamic view into the dictionary. Which means when the dictionary chnages the view reflects these changes

players = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}
print(players.keys())
#Retunrs dict_keys(['ss, '2b', '3b', 'DH', 'OF'])
#The dict_keys before the list wrapping the values in () signifies the object is wrapped but may being viewed
#The Python docs review the dictionary view objects 

player_names = (players.values())
#Returns the values as a viewable object in a list
#Returns in a tuple as an immutable object

player_names = (players.items())
#Returns both the keys and the values (all items) as viewable objects
#Returns in a tuple as an immutable object

#If you try to treat it as a list it will throw an error. View objects may be viewed only, wrapped in a tuple
#Dict values DO NOT support indexing

#To use the items as a list you must cast list onto the variable you want to call within the key:value pair
#You may also COPY the list
#The copy is stored only by the user using the data and may be edited.
#The data many be worked on individually without it being updated as an object by the whole
player_names = list(players.copy().items()


teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels" :  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

#Nested items
#Returns dict view object as a tuple with the items
team_groupings = teams.items()

#May refer to documentaion to see how items may be viewed
#ie. len function allows you to see how many elements are inside
team_groupings = (len(teams_groupings)

#Dict view items are iterable which is very useful for being able to query data
  

"""
[
  ('astros', ['Altuve', 'Correa', 'Bregman']),
  ('angels', ['Trout', 'Pujols']),
  ('yankees', ['Judge', 'Stanton']),
  ('red sox', ['Price', 'Betts'])
]
"""

team_groupings = teams.items()
#Cast as a list
print(list(team_groupings)[1][1][0])
#Indexs may be grabbed. May also grab nested collection. All the way to an individual item in the list