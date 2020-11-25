#How to Add New Key/Value Pairs to Python Dictionaries

teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
}

teams['red sox'] = ['Price', 'Betts']
#Using strings allows for multipe words as a key. Best to keep them as explicit and clear as possible
##To add new items, in this example, the team is placed in a list after the variable to add the key and then assigned it's pair

print(teams)
#Returns the new teams with it's list of players as it's value pair