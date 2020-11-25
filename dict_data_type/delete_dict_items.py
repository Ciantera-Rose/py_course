#Overview of the Multiple Methods for Deleting Items in a Python Dictionary

teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

del teams['angels']
#Use del keyword, pass in name of dict and use dict lookup syntax
#Delets team from dictionary

print(teams.get('No team found by that name'))
#May use get function to see if team exists

teams.pop('astros', 'No team found by that name')
#Pass in name of element you want to remove and a default if team is not found
#Works like get with the nice side effect of removing item from dictionary

removed_team = teams.pop('mets', 'Team not found')
#If item does not exist Python will throw an error. Set default to prevent breaking code
#pop returns value of the lookup or the value of the default element


print(teams)
print(removed_team)