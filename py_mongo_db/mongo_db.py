#Mongo Database Coding Challenge
'''
Create a new Mongo Database.
Create a new Collection in the db, and load 6 documents into it all at once.
Show how to delete the 3rd and 5th documents, and show how to verify only 4 docs exist after.

'''

db.cocktails.insert({
    "name": "Inventory",
    "Date": new Date(),
    "drinks": [
      {"name": "Old Fashioned"},
      {"name": "Mezcal Margarita"},
      {"name": "Manhattan"},
      {"name": "Vodka Martini"},
      {"name": "Madagascar Sour"},
      {"name": "Daiquiri"},
    ]
  })

db.cocktails.insertMany([
    {
      "name": "Old Fashioned",
      "publishedDate": new Date(),``
      "liquor": [
        { "type": "Whiskey" }
      ]
    },
    {
      "name": "Mezcal Margarita",
      "publishedDate": new Date(),
      "liquor": [
        {"type": "Mezcal"}
      ]
    },
    {
      "name": "Manhattan",
      "publishedDate": new Date(),
      "liquor": [
        {"type": "Whiskey"}
      ]
    },
    {
      "name": "Vodka Martini",
      "publishedDate": new Date(),
      "liquor": [
        {"type": "Vodka"}
      ]
    },
    {
      "name": "Madagascar Sour",
      "publishedDate": new Date(),
      "liquor": [
        {"type": "Rum"}
      ]
    },
    {
      "name": "Daiquiri",
      "publishedDate": new Date(),
      "liquor": [
        {"type": "Rum"}
      ]
    },

  ])

  db.cocktails.find(
    {
      name: "Mezcal Margarita"
    },
    {
      _id: 0,
      name: 1,
      liquor: 1
    }
  ).pretty()

  db.cocktails.remove({name: "Manhattan"})
  db.cocktails.remove({name: "Madagascar Sour"})

  db.cocktails.find().pretty()