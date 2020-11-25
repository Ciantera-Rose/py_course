#Guide to Using the get Function in Python Dictionaries to Configure Fallback Lookup Values

teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ['Price', 'Betts'],
}

featured_team = teams.get('mets', 'No featured team')
#If you try to grab a key that doesn't exist Python will throw an error. 
#Setting a default value is a great option as a fallback to prevent the site breaking
#get takes two arguments. 
#Checks for "mets", does not find it and returns "No featured team"

featured_team = teams.get('yankees', 'No featured team')
#Returns list of values paired with the yankees team key

print(featured_team)