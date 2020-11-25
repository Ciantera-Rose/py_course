# Guide to Nested Collections in Python Dictionaries
#In this example we have lists with nested players as the values in the key:value pair

teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
}

astros = teams['astros'] 
#Returns the list of values associated with the key. 
#["Altuve", "Correa", "Bregman"]

astros = (teams['astros'][2])
#Returns the value aof index 2 inside the list.
#"Bregman"

print(astros)

print(teams['angels'])
#Returns list of values for angels
#["Trout", "Pujols"]

print(teams['yankees'])
#Returns list of values for yankees
#["Judge", "Stanton"]