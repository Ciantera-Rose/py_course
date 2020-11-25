#Guide to Working with Lists of Nested Dictionaries
#A list that contains various dictionaries
#Each element of the list contains a team dictionary
#SO...
#We have variable named teams which stores a list
#The list contains multiple dictionaries
#Each one of the dictionaries contains a key value pair with more nested collections
#The key is the team name and inside of that are the various elements
#To traverse them take it one element at a time when you need to query the data for items

teams = [
  {
    'astros': {
      '2B': 'Altuve',
      'SS': 'Correa',
      '3B': 'Bregman',
    }
  },
  {
    'angels': {
      'OF': 'Trout',
      'DH': 'Pujols',
    }
  }
]

print(teams[0])

angels = teams[1].get('angels', 'Team not found')
print(angels)

print(list(angels.values())[1])